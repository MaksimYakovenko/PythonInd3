import numpy as np


def max_min_value_v1(x, n):
    if n == 1:
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                return np.min(np.max(x[i][j]))


def max_min_value_v2(x, n):
    axis = 0 if n == 2 else 1
    return np.min(np.max(x), axis=axis)


if __name__ == '__main__':
    arrays = np.array(
        [
            [1, 2, 3],
            [-1, 4, 5],
            [-2, -8, 9]
        ]
    )
    print(arrays)
    print(max_min_value_v2(arrays, 2))
    print(max_min_value_v1(arrays, 1))