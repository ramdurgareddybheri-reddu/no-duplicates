numbers=[5,6,5,8,5,4,5,8,47,6,2,1,2,1,33,2,33,455,22,20,55,220,455]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)