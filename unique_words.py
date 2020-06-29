str = 'my name is arda, I love my name. '
def count_words(string):
    words = string.split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word]+=1

    print(f'Total Words {len(words)}')
    for word in counts:
        print(f'{word}  {counts[word]}')


count_words(str)