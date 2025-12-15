def to_lower(word):
    aux=""
    word= list(word)
    for i in word:
        if i.isupper():
            i= i.lower()
        aux+=i
    return aux


def count_words(text):
  text=text.split()
  ind= len(text)
  for i in range(ind):
      text[i]= to_lower(text[i])
  return len(set(text))
print(ord('z')-ord('a'))