# Named Indexes
txt1="Welcome to Python {fname} {lname}".format(fname="String",lname="Format")
txt5="Welcome {b} Python {a} Format".format(a="String",b="to")
# Numbered Indexes
txt2="Welcome to Python {0} {1}".format("String","Format")
txt4="Welcome to Python {1} {0}".format("String","Format")
# Empty PlaceHolder
txt3="Welcome to Python {} {}".format("String","Format")
print(txt1)
print(txt5)
print(txt2)
print(txt4)
print(txt3)
