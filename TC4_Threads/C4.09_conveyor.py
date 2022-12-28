import threading
from time import sleep, time
import random
import logging


logging.basicConfig(level=logging.DEBUG)

N = 2
semaphore = threading.Semaphore(N)
lock = threading.Lock()
start = time()
K = 1
result = 0
q = 0


def log(message):
    t = time() - start
    name = threading.current_thread().name
    logging.debug("[%6.3f] %s: %s", t, name, message)


def detail(trans_time, arr_time):
    global q, result, come_time
    sleep(arr_time)
    log("прибула до заводу")
    with lock:
        q += 1
        if q == K:
            log(f"В черзі {K} чи більше деталей")
            come_time = time()
    with semaphore:
        with lock:
            if q == K:
                result += time() - come_time
                log(f"В черзі менше {K} деталей")
            q -= 1
        log(f"потрапила на конвеєр")
        sleep(trans_time)
    log("зійшла з конвеєра")
    print(f"{threading.current_thread().name} зійшла з конвеєра.")


if __name__ == '__main__':
    n = 5
    T1 = 3
    T2 = 5
    T3 = 0
    T4 = 20
    threads = []

    for i in range(n):
        arrive_time = random.random() * (T2 - T1) + T1
        transit_time = random.random() * (T4 - T3) + T3
        thread = threading.Thread(
            name=f"Деталь {i}",
            target=detail,
            args=(arrive_time, transit_time)
        )
        threads.append(thread)
        print(
            f"Деталь {i} надходить до конвеєру о {arrive_time:6.3f} та "
            f"проходить конвеєр за {transit_time:6.3f}"
        )
    for i in range(n):
        threads[i].start()
    for i in range(n):
        threads[i].join()
    log("всі деталі пройшли конвеєр")
    print(f"сумарний час в черзі на проходження конвеєру: {result} секунд")

