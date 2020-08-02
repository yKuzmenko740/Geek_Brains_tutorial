from collections import defaultdict

a = defaultdict()
print(a)

s = "gfdddfsfassaafdsfcxvfgjsdkgvkjgjksdgsdhkjsdisdhvkjxhuukjccjbkssy"
b = defaultdict(int)
for i in s:
    b[i] += 1

print(b)

list_1 = [("cat", 2), ("dog", 5),("cat", 1),("cat", 1)]
c = defaultdict(list)
for k,v in list_1:
    c[k].append(v)
print(c)

f = defaultdict(lambda: "unkmown")
f.update(rex="dog", tomas='cat')
print(f)
print(f['rex'])
print(f["jerry"])