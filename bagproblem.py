#类似背包问题
a = (1, 2, 3, 4, 5, 8)
aim = 10

def make(a, aim, b):
        num = len(a)
        if 0 == num:
                return
        for i in range(num):
                c = list(b)
                sub_aim = aim - a[i]
                c.append(a[i])
                if sub_aim == 0:
                        print c
                elif sub_aim > 0:
                        if num > i + 1:
                                make(a[(i + 1):], sub_aim, tuple(c))

b = []
make(a, aim, b)
print 'sdf'


