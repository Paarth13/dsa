listOfCoinTypes={'Quarter':25,'Dime':10,'Cents':1}
#General approach Returning the coins
# def minCoins(value):
#     missing_value={}
#     for i,x in listOfCoinTypes.items():
#         count=0
#         if value//x>0:
#             count=value//x
#             value%=x
#         missing_value[i]=count
#     return missing_value

#returning min number of coins when on of the entities is missing
#For eg : In case of 31 => ans would be 7(1 quarter and 6 Cents) But min would be 4(3 dimes 1 cent)
def minCoins(value):
    lOfVal=[]
    valu1=value
    valueOfCoins=[25,10,1]
    for i in range(0,len(listOfCoinTypes)):
        missing_value={}
        count=0
        for j in range(i,len(listOfCoinTypes)):
            if value//valueOfCoins[j]>0:
                count=value//valueOfCoins[j]
                value%=valueOfCoins[j]
            missing_value[str(j)]=count
        value=valu1
        lOfVal.append(missing_value)
    return lOfVal
    

def main():
    print (minCoins(31))
if __name__ == "__main__":
    main()

    #quarter is 25c , dime is 10c , penny 1c,nickel is 5c