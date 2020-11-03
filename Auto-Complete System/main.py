# import libraries
import app

corpus = '''I like cat. !
            This dog is like mouse.'''

def suggest_words(user_sent):
    acs = AuComSys(corpus)
    print(acs.vocab)
    print(acs.sent_corpus)
    print('------------------------')
    print(acs.word_corpus)

suggest_words("Hello world!")