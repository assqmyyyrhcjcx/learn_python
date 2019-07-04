import time
import threading
from concurrent.futures import ThreadPoolExecutor


def target():
    for i in range(5):
        print('running thread-{}:{}'.format(threading.get_ident(), i))
        time.sleep(1)


#: 生成线程池最大线程为5个
pool = ThreadPoolExecutor(5)

for i in range(100):
    pool.submit(target)  # 往线程中提交，并运行
