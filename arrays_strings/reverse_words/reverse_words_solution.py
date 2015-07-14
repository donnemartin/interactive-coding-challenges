#solution for reverse words on a string

def reverse_words (S):
  if len(S) is 0:
    return None

  S = S.split()
  for i in range (len(S)):
    S[i] = S[i][::-1]

  return " "join(S)




