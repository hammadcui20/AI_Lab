st=input("Enter a string")
count=0
count_l=0
for i in range(len(st)):

    if st[i].isupper()==True:

        count +=1
    else:
        count_l +=1

print(count_l)
print(count)