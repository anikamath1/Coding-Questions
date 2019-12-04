import math
def findClosestSum(sorted_array,x):
	difference=1000000
	start=0
	result_start_index=0
	result_end_index=0
	end=len(sorted_array)-1
	while(start<end):
		if(math.fabs(sorted_array[start]+sorted_array[end]-x)<difference):
			#print(difference)
			difference=math.fabs(sorted_array[start]+sorted_array[end]-x)
			result_start_index = start
			result_end_index = end
		if(sorted_array[start]+sorted_array[end]>x):
			end=end-1
		else:
			start=start+1
	return (result_start_index,result_end_index)


sorted_array=list(map(int,input("Enter the comma separated sorted array: ").split(",")))
x=int(input("Enter sum: "))
a,b=findClosestSum(sorted_array,x)
print("The closest pair is: ",sorted_array[a],",",sorted_array[b])
