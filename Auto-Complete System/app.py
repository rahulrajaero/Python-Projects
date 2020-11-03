import nltk
import pandas as pd
import numpy as np
import utils

class AutoCompleteSystem:
	def __init__(self, corpus, n=4):
		self.corpus = corpus
		self.n = n
		self.sent_corpus = list(map(lambda a: [a], nltk.sent_tokenize(corpus)))
		self.word_corpus = list(map(lambda a: nltk.word_tokenize(a), [a[0] for a in self.sent_corpus]))
		self.vocab, self.vocab_list, self.vocab_size = utils.get_vocabulary(self.word_corpus)


	def p(self,word):
		return self.vocab.get(word[0], 0)/self.vocab_size


	# define the count function
	def count(self, sentence):
		perm = (len(sentence)-1) + 2

		c = 0
		c += self.m._get_value(('<s>',), tuple(sentence))
		c += self.m._get_value(tuple(sentence), ('</s>',))

		# iterate through the matrix
		for i in range(1, perm-1):
			c += self.m._get_value(tuple(sentence[:i]), tuple(sentence[i:]))

		return c

	def probability(self, sentence, k=1):
		if len(sentence) == 1:
			return self.p(sentence)

		# apply k-smoothing
		sentence_minus_one = sentence[:-1]
		return ((self.count(sentence) + k)/(self.count(sentence_minus_one) + k*self.vocab_size))*probability(sentence_minus_one)

	def get_n_gram(self):
		start_token = ['<s>']*self.n
		end_token = ['</s>']

		res = {}
