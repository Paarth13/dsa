"""Input: exp = “[()]{}{[()()]()}” 
Output: Balanced
[({)]
Input: exp = “[(])” 
Output: Not Balanced
"""
def solve(inp):
    s1=[]
    dic={")":"(","}":"{","]":"["}
    # s1,s2,s3=[],[],[]
    for i in inp:
        if i in dic and s1:
            if s1[-1]==dic[i]:
                s1.pop()
            else:
                return "Unbalanced"
        else:
            s1.append(i)
    if s1:
        return "Unbalanced"
    return "Balanced"
    # for i in inp:
    #     if i=="{":
    #         s1.append("{")
    #     elif i=="(":
    #         s2.append("(")
    #     elif i=="[":
    #         s3.append("[")
    #     elif i=="}":
    #         if s1:
    #             s1.pop()
    #         else:
    #             return "Unbalanced"
    #     elif i=="]":
    #         if s3:
    #             s3.pop()
    #         else:
    #             return "Unbalanced"
    #     elif i==")":
    #         if s2:
    #             s2.pop()
    #         else:
    #             return "Unbalanced"
    # if s1 or s2 or s3:
    #     return "Unbalanced"
    return "Balanced"

if __name__=="__main__":
    print(solve("({(}))"))