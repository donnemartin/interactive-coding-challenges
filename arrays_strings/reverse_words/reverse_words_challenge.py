class ReverseWords:

    def reverse(self, string):
        if string is None:
            return None
        if string == ['']:
            return ['']
        buff_w = []  # buffer for substrings
        substring = []  # substring
        new_string = []  # new string with reverses words
        for i in range(len(string)):
            if(string[i] == ' '):
                for h in range(len(buff_w) - 1, -1, -1):
                    substring.append(buff_w[h])
                for j in range(len(substring)):
                    new_string.append(substring[j])
                substring = []
                buff_w = []
            else:
                buff_w.append(string[i])
                if(i == (len(string) - 1)):
                    new_string.append(' ')
                    for h in range(len(buff_w) - 1, -1, -1):
                        substring.append(buff_w[h])
                    for j in range(len(substring)):
                        new_string.append(substring[j])
        return new_string


def main():
    R = ReverseWords()
    result = R.reverse('foo bar')
    print(result)


if __name__ == "__main__":
    main()
