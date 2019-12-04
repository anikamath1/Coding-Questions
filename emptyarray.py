def merge(array1,array2):
	#to get the index of the last entered element which is not NA
	a=array1.index(-1)-1
	b=len(array2)-1
	last_item=len(array1)-1
	while(b>=0):
		if(a>=0 and array1[a]>array2[b]):
			array1[last_item]=array1[a]
			a-=1
		else:
			array1[last_item]=array2[b]
			b-=1
		last_item-=1

import numpy as np
array1=list(map(int,input("Enter the space separated larger array: enter -1 for blank entries \n").split(" ")))
array2=list(map(int,input("Enter the space separated smaller array; \n").split(" ")))
merge(array1,array2)
print("Merged array is : ",array1)

