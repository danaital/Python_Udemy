list1 = list()
with open("C:\\Users\\Ophir Danai\\.PyCharmEdu2018.3\\config\\scratches\\sample.txt") as file1:
    lines = file1.readlines()
    str1 = ""
for line in lines:
    for word in line.split():
        for char in word:
            if (char not in "`:,.;'!@#$%^&&*()?><_-+=") and char != '"':
                str1 += char
        list1.append(str1.lower())
        str1 = ""
list1.sort()
for word in list1:
    print(word)

print("\n" * 3)
lastword = ""
count = 1
list2 = list()
list3 = list()
for word in list1:
    if lastword == word:
        count += 1
    else:
        str2 = "" + lastword + " " + str(count)
        list3 = list(str2.split())
        tupl = tuple(list3)
        if len(tupl) == 2:
            list2.append(tupl)
        lastword = word
        count = 1
for tup in list2:
    wor, num = tup
    print("The word {} appears {} time in sample.txt".format(wor, num))

print("\n"*5)

samp1 = open("sample1.txt","w")
with open("sample.txt","r") as samp:
    list4 = samp.readlines()
    for liner in list4:
        print(liner.strip("\n"),file=samp1)
samp1.close()
with open("C:\\Users\\Ophir Danai\\.PyCharmEdu2018.3\\config\\scratches\\sample1.txt","a") as sample1:
    for i in range(1,13):
        for j in range (2,13):
            print("{1:>2} times {0} equals {2}".format(i,j,i*j),file=sample1)
        print("="*40,file=sample1)


with open("C:\\Users\\Ophir Danai\\.PyCharmEdu2018.3\\config\\scratches\\sample1.txt","r") as sample1:
    list4 = sample1.readlines()
    samp1 = open("sample1.txt","w")
    for line1 in list4:
        print(line1,end="")


# challenge 11
