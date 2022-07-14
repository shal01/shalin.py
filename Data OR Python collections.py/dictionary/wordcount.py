# hello hi hello hi world
# count={"hello":2,"hi":2,"world":1}

s=input("enter string") #hello hi hello hi hello
count={}
data=s.split(" ")                #['hello','hi','hello','hi','hello']
# print(data)
for word in data:                  #'hello'
    if word not in count:
        count.update({word:1})      #{'hello':1,'hi':1,'world':1}
    else:
        val=count[word]              #val=1
        val+=1                       #val=2
        count.update({word:val})     #{'hello':2,'hi':2}
print(count)