#Pig Latin Transformer

def pig_latin(word):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
	if(word[0] in vowels):
			new_word = word + 'hay'
	else:
		a = word[0]
		new_word = word[1:]
		new_word = new_word + a + 'ay'
	print (new_word)
	return

word = raw_input('Please type a word: ')
pig_latin(word)

