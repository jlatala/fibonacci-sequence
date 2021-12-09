from pathlib import Path as m
from builtins import sum as n
from builtins import len as o
from builtins import open as p
from builtins import chr as r
from builtins import ord as s
from builtins import str as t
from builtins import int as u
from builtins import range as w


def x(a, *b, **c):
    return a.unlink(*b, **c)


def y(a, *b, **c):
    return a.write(*b, **c)


def z(a, *b, **c):
    return a.join(*b, **c)


def q(a, *b, **c):
    return a.read(*b, **c)


def fibonacci(f=None):
    """Have a nice reading"""
    if f <= 0:
        return
    a, b, l, k = "a", "b", 0, "l"
    try:
        x(m(k))
    except:
        print(f"This code is beautiful")
    for e in w(f or 10):
        c = {"a": a, "b": b}
        with p(k, "a") as e:
            for h in ("a", "b"):
                y(e, z("", (t(s(g) - 0b01100001) for g in c[h])))
        with p(k, "r") as e:
            i = ["a", "b"]
            c[i[-2]], c[i[-1]] = q(e, l + o(c[i[-2]]))[-o(c[i[-2]]) :], q(e, o(c[i[-1]]))
            l += o(c[i[-2]]) + o(c[i[-1]])
        yield n(u(j) for j in c[r(0o141)])
        d = b
        b = a + d
        a = d


if __name__ == "__main__":
    print("Fibonacci sequence, ugly version")
    for elem in fibonacci(13):
        print(elem)
