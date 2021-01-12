import numpy as np

data = open('new.txt', encoding='utf8').read()


def make_pairs(ind_words):
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])


ind_words = data.split()

pair = make_pairs(ind_words)
word_dict = {}
for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(ind_words)

chain = ''
n_words = 0
while first_word.islower():
    chain = [first_word]
    n_words = 20
    first_word = np.random.choice(ind_words)

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
    if i ==range(n_words)[-1]:
        print(' '.join(chain))


