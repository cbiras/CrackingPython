def return_unique(arr):
    if len(arr) > 128:
        return False
    frecventa = [0 for i in range(128)]
    for i in arr:
        frecventa[ord(i)] += 1
        if frecventa[ord(i)] > 1:
            return False
    return True

if __name__=='__main__':
    print(return_unique('aba'))