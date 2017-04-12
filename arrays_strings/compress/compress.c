#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *compress (char *s);
char *_calc_partial_result (char p_char, char count);
int main ( ){
  printf("%s\n",compress("AABBCC"));
  return 0;
}


char *compress ( char *s){
  char *result = (char*) malloc(strlen(s)); // result string
  char prev_char; // previous char
  int count = 0; // count defines
  char *p_count;
  int i;
  if(sizeof(s) == 0)
    return NULL;
  prev_char = s[0];
  for (i=0; i<strlen(s); i+=1){
    if (s[i] == prev_char)
      count+=1;
    else{
      asprintf(&p_count, "%i", count);
      strcat(result, _calc_partial_result(prev_char, *p_count));
      prev_char = s[i];
      count = 1;
    }
  }
  asprintf(&p_count, "%i", count);
  strcat(result, _calc_partial_result(prev_char, *p_count));
  if(strlen(result)<strlen(s))
    return result;
  else
    return s;
}

char *_calc_partial_result (char p_char, char count){
  char *buff;
  int c = atoi(&count);
  if(c > 1){
    buff = (char*) malloc(sizeof(p_char) + sizeof(count));
    strcpy(buff, &p_char);
    strcat(buff, &count);
  }else{
    buff = (char*) malloc(sizeof(p_char));
    strncpy(buff, &p_char, sizeof(p_char));
  }
  return buff;
}
