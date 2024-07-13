# For string iteration mostly used for loop
a = "ENJOY LIFE"
t = len(a)
print(t)   # Output 10
for i in range(t):
    print(i)  # Output 0 to 9

for i in range(t):
    print(a[i]) # Output E to F (Whole String)

print(a)  # Output "ENJOY LIFE"
print()
a = a[-1::-1]   # Reverse
print(a) # Reversed Output "EFIL YOJNE"

for i in range(t-1,-1,-1):
    print(a[i])  # Reversed Output "ENJOY LIFE"
print()
for i in range(t-1,-1,-1):
    print(a)    # Reversed Output "EFIL YOJNE"
print()
b = "MR ERROR 313"
for i in b:
    print(i)
