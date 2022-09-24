#process[][0] - Process ID
#process[][1] - Arrival Time
#process[][2] - Burst Time
#process[][3] - Completion Time
#process[][4] - Waiting Time
#process[][5] - Turnaround Time


def swap(process,i,j):
	for k in range(6):
		process[i][k], process[j][k]=process[j][k], process[i][k]


def arrange_arrival_time(process,num):
	for i in range(num):
		for j in range(num-i-1):
			if(process[j][1]>process[j+1][1]):
				swap(process,j,j+1)


def arrange_completion_time(process,num):
	process[0][3]=process[0][1]+process[0][2]  #Completion Time = Arrival Time + Burst Time
	process[0][5]=process[0][3]-process[0][1]  #Turnaround Time = Completion Time - Arrival Time
	process[0][4]=process[0][5]-process[0][2]  #Waiting Time = Turnaround Time - Burst Time
	completion_time=process[0][3]
	i=1
	while(i<num):
		temp=process[i-1][3]
		low=process[i][2]
		
		j=i
		val=i
		while(j<num):
			if(temp>=process[j][1]):
				if(low>process[j][2]):
					low=process[j][2]
					val=j
				elif(low==process[j][2]):
					if(process[val][1]>process[j][1]):
						low=process[j][2]
						val=j					
			
			j=j+1
		
		x=process[val][1]-completion_time
		if(x<=0):
			x=0	
		
		process[val][3]=temp+process[val][2]+x  #Completion Time = Arrival Time + Burst Time
		completion_time=process[val][3]
		process[val][5]=process[val][3]-process[val][1]  #Turnaround Time = Completion Time - Arrival Time
		process[val][4]=process[val][5]-process[val][2]  #Waiting Time = Turnaround Time - Burst Time
		
		swap(process,val,i)
		i=i+1


def SJF(process,num):
	print("\nBefore Arrange...\n")
	print("Process ID\tArrival Time\tBurst Time\n")
	
	for i in range(num):
		print(process[i][0],"\t\t",process[i][1],"\t\t",process[i][2])
	
	arrange_arrival_time(process,num)
	arrange_completion_time(process,num)
	completion_time=0
	print("\nAfter Arrange...\n")
	print("Process ID\tCompletion Time\n")
	
	i=0
	while(i<num):
		if(process[i][1]<=completion_time):
			print(process[i][0],"\t\t",process[i][3])
			completion_time=process[i][3]
			i=i+1
		else:
			print(-1,"\t\t",process[i][1])
			completion_time=process[i][1]


x=input("Enter number of Processes : ")
num=int(x)
process=[]

for i in range(num):
	a=[]
	a.append(int(input("Enter Process ID : ")))
	a.append(int(input("Enter Arrival Time : ")))
	a.append(int(input("Enter Burst Time : ")))
	a.append(int(0))
	a.append(int(0))
	a.append(int(0))
	process.append(a)

SJF(process,num)
