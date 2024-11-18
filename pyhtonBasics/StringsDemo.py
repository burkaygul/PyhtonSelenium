str = "BurkayGuel.com"
str1 = "Consulting firm"
str2 = "BurkayyGuel"
print(str[1]) # u

print(str[0:6]) # Burkay # if you want substring in pyhton

print(str + str1) # concatenation

print(str2 in str) # substring check

var = str.split(".")
print(var)
print(type(var))

print(var[0])

str3 = "    great     "
#print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())