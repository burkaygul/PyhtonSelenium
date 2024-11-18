
greeting = "Good Morning"
a = 4

if a > 2:
    print("Condition matches")
else:
    print("Condition does not match")

print("if else condition code is completed")

# for loop

obj = [2,3,5,7,9]

for i in obj:
    print(i*2)

# sum of First Natural numbers 1+2+3+4+5  = 15

# for(i=1;i<=5;i++)

sum = 0
#range(i,j) i to j-1
for j in range(1,6):
    sum += j

print(sum)
print("***************************")
for k in range(1,10,5):
    print(k)

print("*********SKIPPING FIRST INDEX******************")
for m in range(10):
    print(m)