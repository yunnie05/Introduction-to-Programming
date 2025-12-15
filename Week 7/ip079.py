def csv_change(text, a, b):
    text=text.split(sep=",")
    a-=1
    b-=1
    (text[a],text[b])=(text[b],text[a])    
    return ",".join(text)