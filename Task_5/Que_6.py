#
# 6.	Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below: 
#       Hello I am a file 
#       Where you need to return the data string 
#       Which is of even length 
#       Make sure you return the content in The same link as it is present.
#

file = open("/Users/pareshmahyavanshi/Desktop/git/Assignment/Task_5/doc.txt","r")
f = file.readline()
for f in file:
    if len(f)%2==0:
        print(f)
    else:
        pass
