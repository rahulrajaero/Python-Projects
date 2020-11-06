import app


corpus = '''I like cat. !
This dog is like mouse.'''

s = app.AutoCompleteSystem(corpus)

print("corpus\n", s.corpus)
print('-------------------------------')
print("Vocab:", s.vocab)
print("V_size:", s.vocab_size)
print('--------------------------------')
print("Sent:\n", s.sent_corpus)
print('--------------------------------')
print("Word_cor: ", s.word_corpus)