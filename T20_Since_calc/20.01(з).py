import numpy as np
import matplotlib.pyplot as plt


@np.vectorize
def func01(n):
    return (1 + 1 / n) ** n


def gety(f, x):
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    plt.figure(figsize=(3, 4))
    if b is None:
        plt.plot(x, y, ".b")
        return x[-1], y[-1]
    else:
        k = -1
        prev = False
        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        if not prev:
            return None, None
        begin = 1 if forall else k

        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")
        plt.xlabel("n")
        plt.ylabel("a(n)")
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])
        return x[k], y[k]


if __name__ == "__main__":
    t = (1, 200, 1)
    x = np.arange(*t)
    y = func01(x)
    b = 2.71  # границя
    eps = 0.01
    x0, y0 = plot_seq(x, y, b, eps, True)
    print(x0, y0)
    plt.show()
