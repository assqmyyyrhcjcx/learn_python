class Singleton(type):
    def __init__(cls, *args, **kwargs):
        print("__init__")
        cls.__instance = None
        super(Singleton, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("__call__")
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class Foo(object, metaclass=Singleton):
    def __init__(self):
        print('sub - init')


print('-'*100)
foo1 = Foo()

print('-'*100)
foo2 = Foo()

print(Foo.__dict__)

print(foo1 is foo2)

print(foo1, foo2)


"""
    1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
    2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""