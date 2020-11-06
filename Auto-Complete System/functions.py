# first import necessary libraries
import nltk
import numpy as np
import pandas as pd


corpus = '''I like cats. !
            This dog is like a mouse.'''
k=1
# get the vocab
def get_vocab(corpus):
    '''
    return a dict e.g {'word1': freq1,
                        'word2': freq2,
                        ...}
    '''
    
    # preprocess the data
    # sent = nltk.sent_tokenize(corpus)
    words = nltk.word_tokenize(corpus)
    
    # remove punctuations and stop words NOT
    
    vocab = {}
    
    for w in words:
        vocab[w] = vocab.get(w,0) + 1
        
    return vocab

vocab_with_freq = get_vocab(corpus)
vocab_with_freq = get_vocab(corpus)
vocab = set([key for key in vocab_with_freq.keys()])

total_words = 0
for val in vocab_with_freq.values():
    total_words += val

def p(word):
    return vocab_with_freq.get(word[0])/total_words

# total_words = sum of all freq values
# use functional programming for above task

def get_n_gram(corpus, n):
    '''
    return: a dictionary of n-grams words with freq (n-gram words are a tuple)
    '''
    
    sent = nltk.sent_tokenize(corpus)
    #print(sent)
    data = []
    # tokenize each sentence into words
    for s in sent:
        data.append(nltk.word_tokenize(s))
    
    start_token = ['<s>']*n
    end_token = ['</s>']
    #print(data)
    #print(start_token, end_token)
    
    res = {}
    # iterate through each sentence in data which is list of list
    for sentence in data:
        # add start and end tokens
        sentence = tuple(start_token + sentence + end_token)
        
        r = len(sentence)-n+1
        if r < 0:
            continue
        for i in range(r):
            t = sentence[i:i+n]
            
            # add this n-gram to dict-res
            res[t] = res.get(t,0)+1
    return res


# make distribution_matrix
def word_dist_matrix(corpus):
    n = 4 # set value, say  n = 4
    
    # get unigram + bigram
    unigram = get_n_gram(corpus, n=1) # dictionary of words
    bigram = get_n_gram(corpus, n=2) # dictionary of bi-gram words
    
    list_of_all_words = []
    for key in unigram.keys():
        list_of_all_words.append(key)
    for key in bigram.keys():
        list_of_all_words.append(key)
    
    l = len(list_of_all_words)
    
    # initialize the matrix
    matrix = np.zeros((l,l))
    m = pd.DataFrame(matrix, index=list_of_all_words, columns=list_of_all_words)
    
    # fill the matrix
    all_word_with_freq = {**unigram, **bigram}
    for row in list_of_all_words:
        for col in list_of_all_words:
            key = row+col # define this function
            m.loc[[row],[col]] = all_word_with_freq.get(key, 0)
    
    return m, list_of_all_words

# define count function
## ! this function won't run since sent is in list convert it to sentence for searching into matrix
def count(sent, m):
    
    
    
    # find all permutations of sent then return the sum of each counts
    perm = (len(sent)-1) + 2
    print('Perm', perm)
    
    c = 0
    print(c)
    print('-------------')
    # let's loop through matrix m
    c += m._get_value(('<s>',),tuple(sent))
    print(c)
    c += m._get_value(tuple(sent),('</s>',))
    print(c)
    
    for i in range(1,perm-1):
        c += m._get_value(tuple(sent[:i]),tuple(sent[i:]))
        print(c)
    return c

m, _ = word_dist_matrix(corpus)
print('-'*20)
print(m)
print()
print('-'*20)
# test the above function
sent = ['I', 'like']
count(sent, m)
print('m.loc[[(\'<s>\',)], [(\'<s>\',)]]', m.loc[[('<s>',)], [('<s>',)]])

# define the probability function
# recursive programming
def probability(sent):
    
    if len(sent) == 1:
        return p(sent)
    
    # apply k-smoothing for prob
    sent_minus_one = sent[:-1]
    return ((count(sent, m) + k)/(count(sent_minus_one, m) + k*total_words))*probability(sent_minus_one)


print('-'*30)
print(sent)
probability(sent)

def suggest_a_word(corpus, user_entered_sent):
    
    prob = [] # (word, probabilty)
    for word in vocab:
        pred_sent = user_entered_sent + ' ' + word
        prob.append(tuple(word, probability(pred_sent)))
    
    # print max 10 suggestion
    # get the index of top 10 prob and put it into suggestion
    return prob

# suggestion = suggest_a_word(corpus, user_entered_sent)
# print(suggestion)

print('-'*25)
user_entered_sent = 'I like'
print(user_entered_sent)
for word in vocab:
    pred_sent = user_entered_sent + ' ' + word
    print(pred_sent)