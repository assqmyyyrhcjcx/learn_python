import time
import threading


class MyThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        print('Thread: {} start at {}'.format(self.name, time.ctime(time.time())))
        # 等待event.set()后，才能往下执行
        self.event.wait()
        print('Thread: {} finish at {}'.format(self.name, time.ctime(time.time())))


threads = []
event = threading.Event()

# 定义五个线程
[threads.append(MyThread(str(i), event)) for i in range(1, 5)]

# 重置event，使得event.wait()起到阻塞作用
event.clear()

# 启动所有线程
[t.start() for t in threads]

print('等待5s...')
time.sleep(5)

print('唤醒所有线程...')
event.set()


"""
事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

    clear：将“Flag”设置为False
    set：将“Flag”设置为True
    wait(timeout): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()
    isSet(): 获取内置标志状态，返回True或False
"""