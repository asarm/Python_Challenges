str = 'string of worlds'

def sort_words(str):
    str = str.lower()
    words = str.split(' ')
    words.sort()
    print(words)

sort_words(str)

i=1
while i<=10:
    print(i)
    i+=1