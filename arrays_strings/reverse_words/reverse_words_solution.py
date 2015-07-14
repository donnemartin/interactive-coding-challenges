#solution for reverse words on a string

def reverse_words (str):
  str = str.split()
  newStr = ""

  for words in str:
    newStr += words[::-1]

  return newStr


