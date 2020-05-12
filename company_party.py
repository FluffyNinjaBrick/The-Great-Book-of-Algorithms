

# TASK -  we have a company with a tree-like structure, ie. there's a boss, his subordinate managers,
#         their workers, their interns, etc. Each of them have a fun level, which makes them, well, more
#         fun at parties. The catch is that a person and his direct subordinate cannot be at the same party.
#         With this in mind, what is the most kickass party this company can organise?


class Employee:
    def __init__(self, fun):
        self.emp = []  # subordinates
        self.fun = fun
        self.f = -1
        self.g = -1

        # find most fun party in employee e's subtree
        def f(e):
            if e.f >= 0:
                return e.f
            x = e.fun
            for s in e.emp:
                x += g(s)
            e.f = max(x, g(e))
            return e.f

        # find most fun party in employee e's subtree, where e isn't going
        def g(e):
            if e.g >= 0:
                return e.g
            e.g = 0
            for s in e.emp:
                e.g += f(s)
            return e.g
