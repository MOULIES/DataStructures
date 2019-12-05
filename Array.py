import array
#declaration of array
a = array.array('i',[])
# a = array.array('i',[1,23,56,4,9])

#initialisation of array
for i in range(int(input('enter size of array'))):
    a.append(int(input('enter element {}'.format(i+1))))

## 1 Traversal
for i in range(len(a)):
    print(a[i])