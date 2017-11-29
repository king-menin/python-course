import math


class HeatEquation(object):
    def __init__(
            self,
            x0=0,
            xN=math.pi,
            u0=math.sin,
            f=lambda t, x: math.cos(t / (x + 0.01)),
            a=1,
            N=1000,
            h=None,
            T=1000,
            tau=None
    ):
        self.x0 = x0
        self.xN = xN
        self.u0 = u0
        self.a = a
        self.N = N
        self.h = h if h else (xN - x0) / N
        # Feel bounds
        self._u0 = list(map(u0, map(lambda i: i * self.h, range(N + 1))))
        self.f = f
        self.T = T
        self.tau = self.h * self.h / 2

    def solve(self):
        grid = [self._u0]
        N = (self.N + 1)
        a = [-self.a / self.h ** 2] * (self.N)
        b = [1 / self.tau + 2 * self.a / self.h ** 2] * N
        for t in range(1, self.T):
            f = []
            for x in range(N):
                f.append(grid[-1][x] / self.tau + self.f(t * self.tau, x * self.h))
            grid.append(self.sweep(a, b, a, f))
        return grid

    @staticmethod
    def sweep(a, b, c, f):
        alpha = [-c[0] / b[0]]
        beta = [f[0] / b[0]]
        n = len(f)
        x = [0] * n
        for i in range(1, n - 1):
            m = (b[i] + a[i - 1] * alpha[i - 1])
            alpha.append(-c[i] / m)
            beta.append((f[i] - a[i - 1] * beta[i - 1]) / m)
        beta.append((f[-1] - a[-1] * beta[-1]) / (b[-1] + a[-1] * alpha[-1]))
        x[-1] = beta[-1]

        for i in reversed(range(n - 1)):
            x[i] = alpha[i] * x[i + 1] + beta[i]

        return x

    pass

if __name__ == "__main__":
    he = HeatEquation()
    res = he.solve()