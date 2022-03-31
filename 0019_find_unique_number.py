#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def uniq1(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

def uniq2(a):
    s = set(a)
    for x in s:
        if a.count(x) == 1:
            return x

def uniq3(q):
    a = sorted(q)
    return a[0] if a[0] != a[1] else a[-1]

from collections import Counter
def uniq4(q):
    return Counter(q).most_common()[-1][0]

def uniq(q):
    q.sort()
    return q[0] if q[0] != q[1] else q[-1]

arr = [0,0,0,6,0,0,0,0,0]
print(uniq(arr))