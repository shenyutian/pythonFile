def trim(str):
    while 1:
        if str[-1:] == " ":
            str = str[0:len(str)-1]
        elif str[:1] == " ":
            str = str[1:len(str)]
        else:
            return str


str = trim("  asdf sdf ssds  ")
print(str)
print(len(str))
