w = "Welcome to Python Program"
# find()
print(w.find('e'))
print(w.find('me'))
print(w.find('e',2))
print(w.find('z'))

# index()
print(w.index('e'))
print(w.index('P',3))

# isalpha() isdigit() isalnum()
w="Welcome"
print(w.isalpha())
print(w.isdigit())
print(w.isalnum())
a="Welcome123"
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
b="123"
print(b.isalpha())
print(b.isdigit())
print(b.isalnum())
a="Welcome@123"
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())