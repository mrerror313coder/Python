# Number *Integer *Float *Complex Number
a = 5
print(a, "is of type ", type(a))
a = 2.0
print(a, "is of type ", type(a))
a = 1 + 2j
print(a, "is of type ", type(a))

# String
a = "This is a string"
print(a, "is of type ", type(a))
a = """ Assalamualikum
            Welcome for ENJOY"""
print(a)

#   List
ln = [1, 3.4, 'Error']
print(ln, type(ln))
ln[1] = 313
print(ln)

#  Tuple
t = (1, 'ENJOY', 1+2j)
print(t, type(t))
t = 5
print(t, type(t))


# Dictionary
d = {
   'course_name':'Data Science',
   'course_Duration':'3 Months'
}
print(d, type(d))
print(d['course_name'])

# Set
s = {1, 2, 3, 4, 5, 1}
print(s, type(s))
 