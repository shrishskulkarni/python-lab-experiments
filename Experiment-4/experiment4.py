a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

a.append(5)
print(a)

a.extend(b)
print(a)

a = b.copy()
print(a)

a.sort(reverse=True)
print(a)

a.insert(2, 4)
print(a)

a.remove(4)
print(a)

b.clear()
print(b)

a[1:2] = [6, 7]
print(a)
