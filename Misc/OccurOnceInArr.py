def FindElementThatOccursOnce(ar):
    val=0
    for i in ar:
        val^=i
    print (val)
def main():
    ar=[1,2,34,1,2]
    FindElementThatOccursOnce(ar)
if __name__ == "__main__":
    main()