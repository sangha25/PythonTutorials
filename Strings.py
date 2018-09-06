from django.template.defaultfilters import upper, lower

name="Avinash Thakur"
# find number of character in string.
Strlen=len(name)
print(Strlen)
# upper case to string
print(upper(name))
#lower case to string
print(lower(name))
title="your marks are {}".format(84)
print(title)
# concat to string
str="California{}".format("Great place to live.")
print(str)
