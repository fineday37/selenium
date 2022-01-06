list1 = [1, [2, 3, 4], 5, 6, [7, [8, 9]]]


def flatten(list2):
    if type(list2) == list:
        for t in range(len(list2)):
            for e in flatten(list2[t]):
                yield e
    else:
        yield list2


for t in flatten(list1):
    print(t)


# encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
for i in yield_test(5):
    print(i, ",")
var = lambda a, b, c: print(a, b, c)
var(1, 2, 3)
test = [[{"kdei": "jdk"}],[{"kdei":"djdk"}]]
for w in test:
    print(w)
    ke = "dke"+ w[0]["kdei"]
    print(ke)
