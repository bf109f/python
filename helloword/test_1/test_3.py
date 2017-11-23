import random
a = 1
count = 0
sumer = 0
while a <= 99:
    if a % 2 == 0:
        sumer += a

    count += 1
    a = random.randint(0, 100)
print("共执行%d" % count + "次")
print("总数%d" % sumer)
# b = random.randrange
# print(b)
# print(a)
# print(type(a))