import threading
from time import sleep
from queue import Queue

q = Queue()

T1 = 0.001
T2 = 0.1
T3 = 0.2


def put(F, T):
    with open(F) as f:
        for i in f.readlines():
            q.put(i)
            sleep(T)


def get(F2, t2):
    with open(F2, "w") as f:
        while not q.empty():
            f.write(q.get())
            sleep(t2)


if __name__ == '__main__':
    f1 = "file.txt"
    f2 = "th1.txt"
    f3 = "th2.txt"
    th1 = threading.Thread(target=put, args=(f1, T1))
    th2 = threading.Thread(target=get, args=(f2, T2))
    th3 = threading.Thread(target=get, args=(f3, T3))
    th1.start()
    th2.start()
    th3.start()
    th1.join()
    th2.join()
    th3.join()
