def find_palindrom(string):
    return list(string) == list(reversed(string))

s = "fsfsf"
print(find_palindrom(s))
