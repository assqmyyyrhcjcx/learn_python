from threading import local, Thread, currentThread

# 定义一个local实例
local_data = local()
# 在主线中，存入name这个变量
local_data.name = 'local_data'


class MyThread(Thread):
    def run(self):
        print("赋值前-子线程：", currentThread(), local_data.__dict__)
        # 在子线程中存入name这个变量
        local_data.name = self.getName()
        print("赋值后-子线程：", currentThread(), local_data.__dict__)


if __name__ == '__main__':
    print("开始前-主线程：", local_data.__dict__)

    t1 = MyThread()
    t1.start()
    t1.join()

    t2 = MyThread()
    t2.start()
    t2.join()

    print("结束后-主线程：", local_data.__dict__)



"""
    主线程中的变量，不会因为其是全局变量，而被子线程获取到；
    主线程也不能获取到子线程中的变量；
    子线程与子线程之间的变量也不能互相访问。    
"""