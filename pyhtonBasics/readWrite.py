
file = open('test.txt')
#read all the contents of file
#read n number of characters by passing parameter
#print(file.read(5))

#read one single line at a time readLine()
#print(file.readline())
#print(file.readline())




# print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#['abc\n', 'bvdsf\n', 'cat\n', 'dog\n', 'elephant\n']

linesList = file.readlines()

for eachLine in linesList:
    print(eachLine)




file.close()
