# def fib(num):
#     n, a, b = 0, 0, 1
#     while n < num:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return None
#
#
# f = fib(10)
# ret = next(f)
# print(ret)
#
# # for i in f:
# #     print(i)


# 使用send方法
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        ret = yield b
        print("------>>>>", ret)
        a, b = b, a + b
        n = n + 1
    return None


f = fib(10)
ret = next(f)
print(ret)
# send的里面的数据传递到22行，给ret，当做yield b 的返回值
# send的结果是下一次调用yield时yield后面的值
ret = f.send("hahahah")
print(ret)
