print("Задание 1")
students = {"Аня": 5, "Борис": 4, "Вера": 3}
print(students["Аня"])

print("Задание 2")
d = {"a": 1, "b": 2, "c": 3}
d["d"] = 4
d["a"] = 10
del d["c"]
print(d)

print("Задание 3")
d = {"a": 1, "b": 2}
key = input()
print(d.get(key, "Нет такого ключа"))

print("Задание 4")
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())
print(d.values())
print(len(d))

print("Задание 5")
products = {"хлеб": 50, "молоко": 80, "сыр": 300}
for name in products:
    print(name, products[name])

print("Задание 6")
products = {"хлеб": 50, "молоко": 80, "сыр": 300}
print(sum(products.values()))
print(max(products, key=products.get))

print("Задание 7")
s = input()
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)

print("Задание 8")
s = input()
d = {}
for w in s.split():
    d[w] = d.get(w, 0) + 1
print(max(d, key=d.get))

print("Задание 9")
d = {"a": 1, "b": 2, "c": 3}
print({v: k for k, v in d.items()})

print("Задание 10")
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
d = dict(zip(countries, capitals))
print(d[input()])