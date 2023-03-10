# 20.14
import numpy as np


def triangle(tri):
    # print(tri)
    tri_shifted = np.roll(tri, 1, axis=2)
    # print(tri_shifted)
    dis = np.sqrt(np.sum((tri - tri_shifted) ** 2, axis=1))
    # print(dis)
    perimeter = np.sum(dis, axis=1)
    # print(perimeter)
    max_value_perimeter = np.max(perimeter)
    print(f"Трикутник з найбільших периметром {max_value_perimeter}")


def count_triangles(pts):
    n = pts.shape[1]
    arrays = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # print(i, j, k)
                arrays.append(
                    pts[:, np.array([i, j, k])]
                )
    triplets = np.stack(arrays)
    contents = triangle(triplets)
    # print(contents)
    return np.sum(contents)


if __name__ == '__main__':
    x = np.array([-1, 1, 0, 0])
    y = np.array([0, 0, -np.sqrt(5), np.sqrt(6)])
    points = np.vstack((x, y))
    # points = np.random.randn(2, 3)
    # print(points)
    count_triangles(points)




