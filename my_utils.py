def find_all(char, str):
    occurences = []
    for i in range(len(str)):
        if(str[i] == char):
            occurences.append(i)
    return occurences
