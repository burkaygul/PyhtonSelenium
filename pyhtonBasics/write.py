#file = open('text.txt')
# file.close()

# read the file and store all the lines in list
# reverse the list
# write the reversed list back to the file

# eger bunu kullanirsak file.close() yapmaya gerek yok otomatik kendisi yapiyor
with open('test.txt', 'r') as reader:
    content = reader.readlines() #[abc,bvdsf,cat,dog,elephant]
    reversed(content) # [elephant,dog,cat,bvdsf,abc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
