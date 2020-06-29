import secrets

def generate_password(num_words):
    with open('wordList.txt','r') as file:
        lines = file.readlines()[0:7751]
        word_list = []
        for line in lines:
            word_list.append(line.split()[1])
    words=[]
    for i in range(num_words):
        words.append(secrets.choice(word_list))

    print(''.join(words))
generate_password(2)