
import threading
import time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread:%\n" % n)
    semaphore.release()


if __name__ == "__main__":

    semaphore = threading.BoundedSemaphore(5)  #最多允许5个线程同时运行
    for i in range(22):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("-----all threads has finished...")

