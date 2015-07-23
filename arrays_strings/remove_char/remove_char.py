
def remove_char (Str, char):
  if char not in Str:
    return None
  
  return Str.replace(char, "")

def remove_char_recur (Str, char):
  if len(Str) == 0:
    return Str
  elif Str[0] == char:
    return remove_char_recur (Str[1:], char)
  else:
    return Str[0] +  remove_char_recur (Str[1:], char)

def main():

  mark = "markmarkmarkmark"
  print(remove_char(mark, 'k'))
  print(remove_char_recur(mark, 'k')

if __name__=="__main__":
  main()
