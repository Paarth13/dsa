import math

"""
We pass a string which gets divided into N parts where N is the number of servers.
All the workings servers return the string they recieve and malfunctionong ones don't return anything.
For eg: if they are 3 servers and last server is not working:

So for input : 111 result will be : 11
We need to identify whether it was the first one, second one or third one which is malfunctioning
Question: To find the index of non working server.
List of servers that are working are marked as 1"""
listOfServers=[1,0,1,1,1,0,1,0,1]
def CheckStatus(StringVal):
    listToBeReturned=[]
    for i in range(0,len(listOfServers)):
        if listOfServers[i]!=0:
            listToBeReturned.append(StringVal[i])
    return listToBeReturned
def GeneratingTheUniqueIdentifier(listOfServers):
    BitsToBeUsed=math.ceil(math.log2(len(listOfServers)))
    lis2=[]
    res=[]
    for i in range(BitsToBeUsed-1,-1,-1):
        for j in range(len(listOfServers)-1,-1,-1):
            if j | (1<<i) == j:
                lis2.append(1)
            else:
                lis2.append(0)
        res.append(CheckStatus(lis2))
        # print (lis2,res)
        lis2=[]
    ans=0
    print (res)
    for i in range(0,len(res[0])):
        for j  in range(0,len(res)):
            ans=(ans<<1)|(res[j][i])
        print (ans)
        ans=0

def main():
    GeneratingTheUniqueIdentifier(listOfServers)
if __name__ == "__main__":
    main()