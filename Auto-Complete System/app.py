import nltk
import pandas as pd
import numpy as np


class AuComSys():
    def __init__(self, corpus, n=4):
        self.corpus = corpus
        self.n = n
    
    sentences = nltk.sent_tokenize(corpus)
    words = []
    for s in sentences:
        s = nltk.word_tokenize(s)
        words.append(s)
    
    def get_vocab(self.corpus):
        '''
        return: dictionary
        '''
        words = nltk.word_tokenize(self.corpus)

        vocab_with_freq = {}
        for w in words:
            vocab_with_freq[w] = vocab_with_freq.get(w, 0) + 1
            
        
        vocab = set([val for val in vocab_with_freq.values()])
        return vocab_with_freq, vocab
    
    vocab_size = map([val for val in vocab_with_freq.values()], sum)

    def p(self, word):
    	return vocab_with_freq.get(word, 0)/vocab_size


    # define the count function
    def count(self, sentence, m):
	    '''
	    args:
	        sentence: list of words
	    return:
	        return integer
	    '''
	    # find the permutation of sentence then return the sum of each counts
	    perm = (len(sentence)-1)+2

	    c=0
	    c += m._get_value(('<s>',), tuple(sentence))
	    c += m._get_value(tuple(sentence), ('</s>',))

	    # loop through the matrix m
	    for i in range(1, perm-1):
	        c += m._get_value(tuple(sentence[:i]), tuple(sentence[i:]))
	    
	    return c

	def get_n_gram(corpus, n):
	    '''
	    return: a dictinary of n_gram with freq
	    '''
	    sentence = nltk.sent_tokenize(corpus)

	    data = []
	    for s in sentence:
	        data.append(nltk.word_tokenize(s))
	    
	    start_token = ['<s>']*n
	    end_token = ['</s>']
	    
	    res = {}
	    # iterate over each sentence in data which is list of list
	    for sent in data:
	        # add start and end tokens
	        sent = tuple(start_token+sent+end_token)
	        
	        r = len(sent)
	        if r<0:
	            continue
	        for i in range(r):
	            t = sent[i:i+n]
	            res[t] = res.get(t,0) + 1
	            
	    return res


	# make distribution matrix
	def word_dist_matrix(corpus, n=4):
	    
	    # get unigram and bigram
	        
	    list_of_all_words = []
	    for key in unigram.keys():
	        list_of_all_words.append(key)
	    for key in bigram.keys():
	        list_of_all_words.append(key)
	    
	    l = len(list_of_all_words)
	    
	    # initialize the matrix
	    matrix = np.zeros((l, l))
	    m = pd.DataFrame(matrix, columns=list_of_all_words, 
	                     index = list_of_all_words)
	    
	    fill_the_matrix(m, unigram, bigram, list_of_all_words)
	    return m, list_of_all_words

	# fill the matrix
	def fill_the_matrix(m, unigram, bigram,list_of_all_words):
	    for row in list_of_all_words:
	        for col in list_of_all_words:
	            key = row + col
	            m.loc[[row], [col]] = all_words_with_freq.get(key, 0)

	def probability(sentence):
		if len(sentence) == 1:
			return p(sentence)

		# apply k-smoothing for probability
		sent_minus_one = sentence[:-1]
		return ((count(sentence)+k)/(count(sentence)+k*vocab_size))*probability(sentence)