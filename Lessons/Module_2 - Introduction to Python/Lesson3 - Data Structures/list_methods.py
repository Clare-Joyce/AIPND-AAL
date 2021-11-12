# len, max, min, and Lists
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

# sorted, join, and Lists
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


# Append and Lists
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))