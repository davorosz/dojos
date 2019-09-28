numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

Max = -44
Min = 106
Avg = 0  

for i in numbers:
    Avg += i
    if Min > i:
        Min = i
    if Max < i:
        Max = i
    
print("The biggest number of the list:",Max)
print("The smallest number of the list:",Min)
print("The avarage of the list:",Avg/len(numbers))
