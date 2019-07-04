class Singleton(object):
    def __new__(cls, *args, **kwargs):
        print('111')
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            print('__new__')
        return cls._instance

    # def __call__(cls, *args, **kwargs):
    #     print('222')
    #     if not hasattr(cls, '_instance'):
    #         cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
    #     print('__call__')
    #     return cls._instance


class Foo(Singleton):
    pass


print('*' * 100)
foo1 = Foo()
print('*' * 100)
foo2 = Foo()

# print(foo1() is foo2())

print(foo1 is foo2)

'''
    非元类中的__call__需要使用对象加括号去调用，类似于函数的调用
'''
