import time
import redis


class RedisLock(object):
    def __init__(self, key):
        # redis的连接，官方推荐ssshi用StrictRedis，而不是Redis
        self.rdcon = redis.StrictRedis(host='127.0.0.1', port=6379, password="", db=1, decode_responses=True)
        print(id(self.rdcon))
        # False代表未加锁，True代表加锁了
        self._lock = False
        # lock名字
        self.lock_key = "%s_dynamic_test" % key

    @staticmethod
    def get_lock(cls, timeout=10):
        while not cls._lock:
            print('try to get lock')
            # 过期时间，将作为lock_key的value
            timestamp = time.time() + timeout + 1
            # 设置lock_key，value为过期时间
            # 注：加锁成功返回Ture，加锁失败返回False
            cls._lock = cls.rdcon.setnx(cls.lock_key, timestamp)

            # 注意下方括号的范围，如果当前时间大于lock_key的value，那么也就是lock_key过期了
            if cls._lock or (time.time() > float(cls.rdcon.get(cls.lock_key)) and
                             time.time() > float(cls.rdcon.getset(cls.lock_key, timestamp))):

                print("get lock")
                break
            else:
                time.sleep(1)

    @staticmethod
    def release(cls):
        # 释放锁资源，即使lock_key未过期，也要释放锁资源
        if time.time() < float(cls.rdcon.get(cls.lock_key)):
            print("release lock")
            cls.rdcon.delete(cls.lock_key)


# 装饰器，用来加锁的装饰器
def deco(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            # 查看对象及地址
            print("before %s called [%s]." % (func.__name__, cls))
            # 装饰器传入的参数为redis的lock对象，调用get_lock方法，同时把自己当作参数传入
            cls.get_lock(cls)
            try:
                return func(*args, **kwargs)
            finally:
                cls.release(cls)

        return __deco

    return _deco


@deco(RedisLock("lock_key"))
def myfunc():
    print("myfunc() called.")
    time.sleep(5)


if __name__ == "__main__":
    myfunc()
