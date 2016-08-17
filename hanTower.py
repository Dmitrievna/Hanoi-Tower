import copy

def change(lst1,lst2,lst3,Num):
    if ( Num == 1 ):
    	#print("before:",lst1,lst2,lst3)
    	lst3.insert( lst3.count(0)+1 ,lst1[lst1.count(0)+1] )
    	lst3.remove(0)
     	lst1.remove(lst1[lst1.count(0)+1])
     	lst1.insert(1,0)
     	print(lst1[0]+" - "+ lst3[0])

    else:
    	#print("before:",lst1,lst2,lst3)
    	#print("1 - 2")
    	change(lst1,lst3,lst2,Num - 1)
    	#print("result:",lst1,lst2,lst3)
    	#print("before:",lst1,lst2,lst3)
    	#print("1 - 3")
        lst3.insert(lst3.count(0)+1,lst1[lst1.count(0)+1])
        lst1.remove(lst1[lst1.count(0)+1])
        lst1.insert(1,0)
        lst3.remove(0)
        print(lst1[0]+" - "+lst3[0])
        #print("result:",lst1,lst2,lst3)
        #print("before:",lst1,lst2,lst3)
        #print("2 - 3")
        change(lst2,lst1,lst3,Num - 1)
        #print("result:",lst1,lst2,lst3)




numberRow = int(input())
s = [list() for x in range(3)]
s[0] = [x for x in range(numberRow+1)]
s[1] = [0 for x in range(numberRow+1)]
s[2] = copy.deepcopy(s[1])
s[0][0] = '1'
s[1][0] = '2'
s[2][0] = '3'
#print(s[0][3])
#test = [list() for x in range(3)]
#test[0] = [1,2,3]
#test[1] = [0,0,0]
#test[2] = [0,0,0]
change(s[0],s[1],s[2],numberRow)