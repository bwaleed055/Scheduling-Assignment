burst_Time=[]
arrival_Time=[]
process_No=[]
finish_Time=[]
waiting_Time=[]

print("Enter the number of process: ")
n=int(input())

i=0
for i in range(n):
    num=int(input("\nEnter Process No: "))
    process_No.insert(i,num)
    ArrivalTime=int(input("Enter arrival time for process: "))
    arrival_Time.insert(i, ArrivalTime)
    BurstTime=int(input("Enter Burst time for process: "))
    burst_Time.insert(i, BurstTime)

for i in range(n):
    for j in range(n-i-1):
        if(arrival_Time[j]>arrival_Time[j+1]):
            
            temp0=process_NO[j]
            process_NO[j]=process_NO[j+1]
            process_No[j+1]=temp0

            temp1=arrival_Time[j]
            arrival_Time[j]=arrival_Time[j+1]
            arrival_Time[j+1]=temp1

            temp2=burst_Time[j]
            burst_Time[j]=burst_Time[j+1]
            burst_Time[j]=temp2

for i in range(n):
    finish_Time = [int(arrival_Time[i] + burst_Time[i]) for i in range(n)]
    waiting_Time=[int(finish_Time[i]-arrival_Time[i]) for i in range(n)]

print("process NO\t\t\tWAiting Time")

for i in range(n):
    print(process_No[i],"\t\t",waiting_Time[i])

sum=0
for i in range(n):
    sum=sum+waiting_Time[i];
   
print("Average Waiting Time",sum/n)






