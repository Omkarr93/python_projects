# 796115110113721110141108

s = '796115110113721110141108'
# 801141011127311011511697
s = s[::-1]
print(s)

res = ""
i = 0
while(i<len(s)-1):
    x = s[i] + s[i+1]
    # print(x)

    if x == "32":
        res = res + " "
    elif int(x) in range(65,91) or int(x) in  (97,123):
        res = res + chr(int(x))
    elif i+2<len(s):
        x = x+s[i+2]
        res = res + chr(int(x))

        i += 1
    i +=2
print(res)



def swap_case(s):
    res = ""
    i = 0
    while i < len(s):  # Removed -1 from the loop condition
        if ord(s[i]) in range(65, 91):  # Used ord() to get the ASCII value of the character
            res = res + s[i].lower()
        else:
            res = res + s[i].upper()
        i += 1  # Incrementing the loop variable

    return res  # Moved the return statement outside of the while loop



