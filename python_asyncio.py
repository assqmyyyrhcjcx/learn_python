import asyncio

"""
    event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
    future 对象： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
    task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。
    async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。
"""


async def hello(name):
    # asyncio.sleep(n)，这货是asyncio自带的工具函数，他可以模拟IO阻塞，他返回的是一个协程对象
    await asyncio.sleep(2)
    print('Hello,', name)
    return 'Hello, ' + name


def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())


# 定义协程对象
coroutine = hello("World")

# 定义事件循环对象容器
loop = asyncio.get_event_loop()

# 将协程转为task任务
task = loop.create_task(coroutine)
# task = asyncio.ensure_future(coroutine)

# 添加回调函数
task.add_done_callback(callback)

# 将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)

# 注：ensure_future可以创建task任务
# 注：可以不将协程对象转为task任务，直接添加到loop循环中

# yield from 后面可接 可迭代对象，也可接future对象/协程对象；
# await 后面必须要接 future对象/协程对象
