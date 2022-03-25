"""
there are 3 operations that can be done on a string:
-insertion of one character
-deletion of one character
-replacement of one character
check if two strings are one operation away
"""

def check(s1,s2):
    if len(s1)==len(s2):
        return check_replacement(s1,s2)
    elif len(s1) + 1 == len(s2):
        return check_insert(s1,s2)
    elif len(s1) - 1 == len(s2):
        #notice here that they are reversed
        return check_insert(s2,s1)
    return False

def check_replacement(s1,s2):
    replaced = False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            if replaced == True:
                return False
            replaced = True
    return True

def check_insert(s1,s2):
    index1,index2 = 0,0
    while index1<len(s1) and index2<len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
    return True

if __name__=="__main__":
    print(check("pale","bake"))