class Log:

    def __init__(self, func):
        print('Log init')
        self.func = func

    def __call__(self, *args):
        print('Log call')
        return self.func(args)
    

@Log
def get_funky(name):
    print(name, 'get funky')


# 类装饰器，相当于func = Log(func)，初始化的时候执行'__init__'方法，参数为被修饰的方法名，类中的'__call__'方法，可以使对象像函数一样执行，例：func()


class PLog:

    def __init__(self, *args):
        print('Log init')
        self.args = args

    def __call__(self, func):
        def get_params(*args):
            print('Log call')
            return func(args)
        return get_params


@PLog('PLog')
def get_funny(name):
    print(name, 'get funny')


# 类装饰器带有参数，plog = PLog('param')，返回是对象plog，并调用了'__init__'方法，且传入了装饰器的参数，调用'__call__'方法，plog()传入方法名以及参数


if __name__ == '__main__':
    get_funky('Log')
    get_funny('PLog')
