def revd(x):
    out=[]
    for i in range(len(x)-1,-1,-1):
        out.append(x[i])
    return ''.join(out)


def main():
    print (revd("hello"))
if __name__ == "__main__":
    main()