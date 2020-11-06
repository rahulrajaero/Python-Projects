def suggest_a_word(self, user_sent):
		prob = []

		for w in self.vocab_list:
			t = user_sent + w
			prob.append(tuple(w, self.probability(t)))
		return prob

	def probability(self, sentence, k=1):
		if len(sentence) == 1:
			return self.p(sentence)

		# apply k-smoothing
		sentence_minus_one = sentence[:-1]
		return ((self.count(sentence) + k)/(self.count(sentence_minus_one) + k*self.vocab_size))*probability(sentence_minus_one)


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

	# word distribution matrix
	def word_dist_matrix(self):
		unigram = self.get_n_gram(n=1) # dictionary of words
		bigram = self.get_n_gram(n=2) # dictionary of bi-gram words
		list_of_all_words = []
		for key in unigram.keys():
			list_of_all_words.append(key)
		for key in bigram.keys():
			list_of_all_words.append(key)

		l = len(list_of_all_words)
		matrix = np.zeros((l,l))
		m = pd.DataFrame(matrix, index=list_of_all_words, columns=list_of_all_words)

		# fill the matrix
		all_word_with_freq = {**unigram, **bigram}
		for row in list_of_all_words:
			for col in list_of_all_words:
				key = row + col
				m.loc[[row], [col]] = all_word_with_freq.get(key, 0)
		return m



	def get_n_gram(self, n):
		start_token = ['<s>']*self.n
		end_token = ['</s>']

		res = {}
		for sent in self.sent_corpus:
			sent = tuple(start_token + sent + end_token)

			r = len(sent)-self.n+1
			if r<0:
				continue
			for i in range(r):
				t = sent[i:i+self.n]

				# add this to n-gram dict
				res[t] = res.get(t, 0) + 1
		return res

	def p(self,word):
		return self.vocab.get(word[0], 0)/self.vocab_size


def main():
	corpus = '''I like cat. !
	This dog is like mouse.'''
	acs = AutoCompleteSystem(corpus)
	user_sent = 'I like'

	suggestion = acs.suggest_a_word(user_sent)
	print(suggestion)

if __name__ == '__main__':
	main()
 