#include <stdio.h>

void Reverse(char* str) {
    if (str) {
        char* i = str;	// first letter
        char* j = str;	// last letter

        // find the end of the string
        while (*j) {
            j++;
        }

        // don't point to the null terminator
        j--;

        char tmp;

        // swap chars to reverse the string
        while (i < j) {
            tmp = *i;
            *i++ = *j;
            *j-- = tmp;
        }
    }
}

int main() {
    char test0[] = "";
    char test1[] = "foo";
    Reverse(NULL);
    Reverse(test0);
    Reverse(test1);
    printf("%s \n", test0);
    printf("%s \n", test1);
    return 0;
}
