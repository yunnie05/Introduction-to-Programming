def palindrome(word):
    n= len(word)-1
    for i in word:
        if i!= word[n]:
            return False
        n-=1
    return True
