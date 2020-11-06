import re



def process_data(filename):

	words = []

	f = open(filename, 'r')
	for line in f:
		line = line.lower()
		temp = re.findall('\w+', line)
		words += temp

	return words


# run the above functin and process some .txt file
word_list = process_data('shakespeare.txt')
# create vocabulary for the above text
vocab = set(word_list)
print(f"The first ten words in the txt file are: \n{word_list[:10]} ")
print(f"Vocab Size: {len(vocab)}")


def get_count(word_list):
	dictionary = {}
	for word in word_list:
		dictionary[word] = dictionary.get(word, 0) + 1

	return dictionary

# Test2 ----------------------------------------------------------------------
word_count_dict = get_count(word_list)
print(f"There are {len(word_count_dict)} key-value pairs.")
print(f"thee: {word_count_dict.get('thee', 0)}")


def get_probs(word_count_dict):
	probs = {}
	M = sum(word_count_dict.values())

	for key in word_count_dict:
		probs[key] = word_count_dict.get(key, 0)/M

	return probs

# Test 3 ---------------------------------------------------------------------
probs = get_probs(word_count_dict)
print(f"Total Probs: {len(probs)}")
print(f"P('thee'): {probs['thee']:.4f}")


# ------------ PART 2 --------------------------------------------------------
# String Manipulation
# delete_letter
# switch_letter
# replace_letter
# insert_letter

def delete_letter(word, verbose = False):
	split_list = [(word[:i], word[i:]) for i in range(len(word))]
	delete_list = [L+R[1:] for L, R in split_list if R]

	if verbose:
		print(f'Input word: {word}\n')
		print(f'Split_list: {split_list}')
		print(f'Delete_list: {delete_list}')

	return delete_list

# Test
delete_letter('cans', verbose=True)


def switch_letter(word, verbose=False):
	split_list = [(word[:i], word[i:]) for i in range(len(word))]
	switch_list = [L[:len(L)-1] + R[0] + L[len(L)-1] + R[1:] for L, R in split_list if L != '' and R != '']
	
	if verbose:
		print(f'Input word: {word}\n')
		print(f'Split_list: {split_list}')
		print(f'Switch_list: {switch_list}')

	return switch_list

# Test
switch_letter('eta', verbose=True)


def replace_letter(word, verbose=False):

	letters = 'abcdefghijklmnopqrstuvwxyz'
	split_list = [(word[:i], word[i:]) for i in range(len(word))]
	replace_list = [L+a+(R[1:] if len(R)>1 else '') for L, R in split_list if R for a in letters]
	replace_set = set(replace_list)
	replace_set.remove(word)
	replace_list = sorted(list(replace_set))

	if verbose:
		print(f'Input word: {word}\n')
		print(f'Split_list: {split_list}')
		print(f'Replace_list: {replace_list}')

	return replace_list

# Test
replace_letter('can', verbose=True)


def insert_letter(word, verbose=False):
	
	letters = 'abcdefghijklmnopqrstuvwxyz'

	# allow the use of empty string '' here
	split_list = [(word[:i], word[i:]) for i in range(len(word)+1)]
	insert_list = [L+a+R for L, R in split_list for a in letters]

	if verbose:
		print(f'Input word: {word}\n')
		print(f'Split_list: {split_list}')
		print(f'Insert_list: {insert_list}')

	return insert_list

# Test
insert_letter('at', True)
print(f"Number of Output: {len(insert_letter('at'))}")

# -------------- PART 3 Combining the edits ----------------------------------

def edit_one_letter(word, allow_switches = True):

	res = delete_letter(word) + replace_letter(word) + insert_letter(word)

	if allow_switches:
		res += switch_letter(word)

	edit_one_set = set(res)

	return edit_one_set

# Test
input_word = 'at'
print(f"input word: {input_word}")
print(f"Number of output: {len(edit_one_letter(input_word))}")
print(f"edit_one_list: \n{sorted(list(edit_one_letter(input_word)))}")


def edit_two_letters(word, allow_switches = True):
	
	res = set()
	res1 = edit_one_letter(word, allow_switches)
	for w in res1:
		if w:
			res.update(edit_one_letter(w, allow_switches))

	return res

# Test
print(f"Number of strings which is two edit away from {'a'}: {len(edit_two_letters('a'))}")
print(f"Number of strings which is two edit away from {'at'}: {len(edit_two_letters('at'))}")

# -------------------PART - 3.3 suggesting spelling correction-------------

# Pyhton SHORT-CIRCUIT
print('-'*20)
print('SHORT CIRCUIT')
print([] and ['a', 'b'])
print([] or ['a'])
print('-'*20)

def get_correction(word, probs, vocab, n=2, verbose=False):

	suggestion = []
	n_best = []

	edit_one = edit_one_letter(word)
	edit_two = edit_two_letters(word)
	edit_intersection = edit_one.intersection(edit_two)
	suggestion = list((word in vocab and word) or edit_intersection.intersection(vocab))
	n_best = [(w, probs[w]) for w in suggestion]

	if verbose:
		print(f"entered_word: {word}")
		print(f"suggestion: {suggestion}")

	return n_best

# Test
my_word = 'dys'
tmp_correction = get_correction(my_word, probs, vocab, 2, verbose=True)
for i, word_prob in enumerate(tmp_correction):
	print(f"word{i}: {word_prob[0]}, probability: {word_prob[1]:.6f}")

print(f"Data Type of Correction: {type(tmp_correction)}")