def url(s):
    s = list(s)
    for i in range(len(s)):
        if s[i]==' ':
            s[i]="%20"
    return "".join(s)

if __name__=="__main__":
    print(url("eu coaie"))