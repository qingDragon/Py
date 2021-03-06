import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)
    print("task down", n)

#
# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()
#

start_time = time.time()
t_objs = [] #存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i,))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()
    t_objs.append(t)  #为了不足赛后面线程的启动，不在这里join，先放到一个列表中

# for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
#     t.join()
time.sleep(3)
print("-----all threads has finished...")
print("cost:",time.time() - start_time)