from ugly_imports import *


def fibonacci(f=0xA):
    """Have a nice reading"""
    if E(f, 0b11 >> 1) <= s("\x00"):
        return
    l, k, F = u(C(None)), A[11], B(A[:2])
    a, b = F
    try:
        x(m(k))
    except:
        print(f"This code is beautiful")
    for e in w(u(f) if H(f) is u else G(f)):
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
        b = D(t(), (a, d))
        a = d


if __name__ == "__main__":
    print("Fibonacci sequence, ugly version")
    for elem in fibonacci(13):
        print(elem)
