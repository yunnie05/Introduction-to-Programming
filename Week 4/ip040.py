def remove_all(word, ch):
    res= ""
    for i in word:
        if i== ch:
            continue
        res+= i
    return res
