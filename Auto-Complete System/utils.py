def get_vocabulary(word_corpus):
	v = {}
	for s in word_corpus:
		for w in s:
			v[w] = v.get(w, 0) + 1

	v_list = []
	vocab_size = 0
	for k, value in v.items():
		v_list.append(k)
		vocab_size += value

	return v, v_list, vocab_size

