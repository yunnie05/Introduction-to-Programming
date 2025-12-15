def count(word, letters):
    count= 0
    for i in letters:
        for j in word:
            if j==i:
                count+= 1
    return count            