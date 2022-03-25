def perm_pali(s1):
    frec = [0 for i in range(128)]
    cnt_imp=0
    for i in s1:
        if i != " ":
            frec[ord(i)]+=1
    for i in frec:
        if i%2 == 1:
            cnt_imp+=1
    if cnt_imp > 1:
        return False
    return True

if __name__== "__main__":
    print(perm_pali("tact coat"))