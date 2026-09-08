def task7(s):
    string_1 = ""
    string_2 = ""
    for i in range(len(s)):
        if(i % 2 != 0):
            string_1 += s[i]
        else:
            string_2 += s[i]
    print(string_1, string_2)
