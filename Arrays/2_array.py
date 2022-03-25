""" 
check if two strings are permutations of each other
1: equal lengths
2: they are the same if they are sorted
"""
def check_perm(s1,s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1)!=sorted(s2):
        return False
    return True

if __name__=='__main__':
    print(check_perm("ab","ba "))