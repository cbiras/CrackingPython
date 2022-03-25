def compress_string(s1):
    compressed = ""
    consecutive = 0
    for i in range(len(s1)):
        consecutive += 1
        if i+1 >= len(s1) or s1[i]!=s1[i+1]:
            compressed += s1[i] + str(consecutive)
            consecutive = 0
    return compressed if len(compressed) < len(s1) else s1

if __name__=="__main__":
    print(compress_string("aabcccccaaa"))