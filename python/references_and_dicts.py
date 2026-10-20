a = [1,2,3]
b=a
b=b.append(4)
print(a)
print(b)
print(a is b)



a = [1,2,3]
b =a
b = b+[4]
print(a)
print(a is b)


c = [1,2]
d = c+ [3]
print(c)
print(c is d)
print(d)


s = "hello"
a = "H"
s = a + s[1:]
print(s)


counts = {"apple": 2, "banana": 5}
counts["apple"] += 1
counts["cherry"] = 1
print(counts)
# print(counts["mango"]) keyError: 'mango'
print("mango" in counts)
print(counts.get("mango"))
print(counts.get("mango",0))
