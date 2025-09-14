s = input("Enter string: ")

print(f"Reversed: {s[::-1]}")
print(f"first and last letter capital {s[0].upper() + s[1:-1] + s[-1].upper()}")
print(f"swapped commas and dots: ", end = "")
for c in s:
    if c == '.':
        print(',', end = "")
    elif c == ',':
        print('.', end = "")
    else:
        print(c, end = "")
print()

print("max count: ", end = "")

cur = (-1, -1)
for c in s:
    cur = max(cur, (s.count(c), c))

print(cur[::-1])