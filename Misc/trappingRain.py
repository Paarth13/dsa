def trap(height):
        prefixArr=[]
        maxVal=height[0]
        for i in height:
            if maxVal<i:
                prefixArr.append(i)
                maxVal=i
            else:
                prefixArr.append(maxVal)
        postfixArr=[]
        maxVal=height[len(height)-1]
        for i in range(len(height)-1,-1,-1):
            if maxVal<height[i]:
                postfixArr.append(height[i])
                maxVal=height[i]
            else:
                postfixArr.append(maxVal)
        # print(prefixArr,postfixArr)
        postfixArr=postfixArr[::-1]
        ind=-1
        maxValue=0
        for i in range(1,len(height)-1):
            calc=max(min(prefixArr[i],postfixArr[i])-height[i],0)
            print(calc)
            maxValue+=calc
        print(maxValue)
def main():
    # height=[0,1,0,2,1,0,1,3,2,1,2,1] // ans =6
    height=[4,2,0,3,2,5] #ans=9
    trap(height)
if __name__ == "__main__":
    main()