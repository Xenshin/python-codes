str = "@Debugging is being the detective in a criminal movie where you are also the murderer"
if str.startswith("@"):
        list = str.split()
        for i in list:
            if "@" in i:
                print(len(i)-1,end=",")
            elif (i == list[-1]):
                print(len(i))
            else:
                print(len(i),end=",")

# second way
str = "@Debugging is being the detective in a criminal movie where you are also the murderer"
list = str.split()
for i in range(len(list)):
    if "@" in list[i]:
        print(len(list[i])-1,end=",")
    elif (i == len(list)-1):
        print(len(list[i]))
    else:
        print(len(list[i]),end=",")