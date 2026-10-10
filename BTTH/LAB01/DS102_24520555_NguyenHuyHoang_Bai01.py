#Newton-Raphson tìm điểm cực trị của f(x, y) = x^4 + y^4 - 4xy.
import numpy as np


def grad(u):
    x, y = u
    return np.array([4 * x**3 - 4 * y,
                     4 * y**3 - 4 * x], dtype=float)


def hessian(u):
    x, y = u
    return np.array([[12 * x**2, -4],
                     [-4, 12 * y**2]], dtype=float)


def newton_optim(u_0, grad_fn, hessian_fn, epsilon=1e-8, max_iter=100):
    u = np.array(u_0, dtype=float)

    for _ in range(max_iter):
        g = grad_fn(u)
        if np.linalg.norm(g) < epsilon:
            break

        t = np.linalg.solve(hessian_fn(u), -g)
        u = u + t

    return u


if __name__ == "__main__":
    u_0 = (10.0, 10.0)
    u_optim = newton_optim(u_0, grad, hessian, epsilon=1e-6, max_iter=100)
    print("Điểm tối ưu tìm được:", u_optim)
