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
		self.vocab, self.vocab_list, self.vocab_size = self.get_vocabulary()
		#self.m = self.word_dist_matrix()


	def get_vocabulary(self):
		v = {}
		for s in self.word_corpus:
			for w in s:
				v[w] = v.get(w, 0) + 1

		v_list = []
		vocab_size = 0
		for k, value in v.items():
			v_list.append(k)
			vocab_size += value

		return v, v_list, vocab_size