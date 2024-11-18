
values = [1,2,"Burkay",4,5.2]
#List is data type that allow multiple values and can be differend data types

print(values[0]) #1

print(values[3]) #4

print(values[-1]) #5.2

print(values[1:3]) # [2, 'Burkay']

values.insert(3, "Hello")

print(values)

values.append("End")

print(values)

values[2] = "BURKAY"

print(values)

del values[0]

print(values)


# Tuple - Same as LIST Data type but immutable
val = (1,2,3, "Burkay")
print(val)

# val[2] = "Hello" # 'tuple' object does not support item assignment

#Dictionary
dic = {"a":2, 4 : "bcd", "c":"Hello World"}

print(dic["a"]) #2
print(dic[4]) #2
print(dic["c"]) #2

#
dict = {}
dict["firstName"] = "Burkay"
dict["lastName"] = "Gül"
dict["age"] = 28
dict["gender"] = "Male"


print(dict)
print(dict["lastName"])
