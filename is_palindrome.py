# level

# race car
str = "Go hang a salami I'm a lasagna hog"

def delete_spaces(str):
    str = str.replace(' ', '')
    return str

def check_pallindrome(str):
    str = delete_spaces(str.lower())
    middle = int((len(str)/2))

    for i in range(middle):
        if(str.count(str[i])) < 2:
            return False
    return True

print(check_pallindrome(str))