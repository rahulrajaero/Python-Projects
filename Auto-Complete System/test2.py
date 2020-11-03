import nltk

c = list(map(lambda x: [x], ['I like', 'cats']))
print(c)

d = list(map(lambda x: nltk.word_tokenize(x), [a[0] for a in [['I like'], ['cat']]]))
print(d)