# print("Задание 1")
# for i in range(1, 11):
#     print(i)

# print("Задание 2")
# for i in range(2, 51, 2):
#     print(i)

# print("Задание 3")
# for i in range(10, 0, -1):
#     print(i)

# print("Задание 4")
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)

# print("Задание 5")
# n = int(input())
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)

# print("Задание 6")
# n = int(input())
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# print("Задание 7")
# nums = [3, -1, 0, 7, -5, 2, 8]
# count = 0
# for x in nums:
#     if x > 0:
#         count += 1
# print(count)

# print("Задание 8")
# s = input()
# vowels = "аеёиоуыэюяaeiouy"
# count = 0
# for ch in s.lower():
#     if ch in vowels:
#         count += 1
# print(count)

# print("Задание 9")
# nums = [3, 9, -2, 9, 5]
# largest = nums[0]
# for x in nums:
#     if x > largest:
#         largest = x
# print(largest)

# print("Задание 10")
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i * j:4}", end="")
#     print()

# print("whele")

# print("Задание 1")
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print("Задание 2")
# total = 0
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     total += x
# print(total)

# print("Задание 3")
# n = int(input())
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print(count)

# print("Задание 4")
# n = int(input())
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)

# print("Задание 5")
# n = int(input())
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# print(rev)

# print("Задание 6")
# n = int(input())
# p = 1
# while p <= n:
#     print(p)
#     p *= 2

# print("Задание 7")
# password = "12345"
# user_input = input()
# while user_input != password:
#     user_input = input()
# print("Доступ разрешён")

# print("Задание 8")
# a = int(input())
# b = int(input())
# while b != 0:
#     a, b = b, a % b
# print(a)

# print("Задание 9")
# n = int(input())
# a, b = 0, 1
# while a <= n:
#     print(a)
#     a, b = b, a + b

# print("Задание 10")
# import random
# secret = random.randint(1, 100)
# attempts = 0
# while True:
#     guess = int(input())
#     attempts += 1
#     if guess < secret:
#         print("Больше")
#     elif guess > secret:
#         print("Меньше")
#     else:
#         print(attempts)
#         break