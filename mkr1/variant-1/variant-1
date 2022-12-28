import numpy as np
import matplotlib.pyplot as plt


def par(x):
    par.__name__ = f"parabola"
    return (x - 1) ** 2


def lin_func(k, l):
    def _lin_func(x):
        return k * x + l
    _lin_func.__name__ = f"linear function"
    return _lin_func


def square(f1, f2, xmin, xmax, ymin, ymax):
    box_square = (xmax - xmin) * (ymax - ymin)
    count = int(box_square * 1000)
    x = np.random.uniform(xmin, xmax, count)
    y = np.random.uniform(ymin, ymax, count)
    y1 = f1(x)
    y2 = f2(x)
    count_in = np.sum(
        # np.logical_or(
        #     np.logical_and(y1 < y, y < y2),
        #     np.logical_and(y2 < y, y < y1)
        # )
        np.logical_and(y2 < y, y < y1)
    )
    if count_in != 0:
        return count_in / count * box_square
    else:
        return "Графіки не перетинаються."


def move_axes():
    a0, b0, c0, d0 = plt.axis()
    d0 = 3 / 8 * (b0 - a0)
    c0 = -2 * d0
    plt.axis((a0, b0, c0, d0))
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    plt.legend(loc="best")


def plot_f1f2(x, f1, f2):
    y1 = f1(x)
    y2 = f2(x)
    plt.plot(x, y1, "-m", lw=2, label=f1.__name__)
    plt.plot(x, y2, "-b", lw=2, label=f2.__name__)
    plt.fill_between(x, y1, y2, where=(y2-y1) >= 0, facecolor="yellow")

    square_between_figure = square(f1, f2, *plt.axis())
    print(square_between_figure)

    move_axes()


def plot_functions(a, b, y1, y2):
    plt.figure(figsize=((b - a) * 3, 4 * (b - a)))
    x = np.linspace(a, b, int(b - a) * 50)
    plot_f1f2(x, y1, y2)

    plt.show()


if __name__ == "__main__":
    a = -20
    b = 20
    k = 2
    l = 0
    plot_functions(
        a, b,
        par,
        lin_func(k, l)
    )
