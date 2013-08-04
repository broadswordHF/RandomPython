pyg = 'ay'
original = raw_input('Please enter a word...')
word = original.lower()
first_letter = word[0]
new_word = word + pyg


if original.isalpha():
	if first_letter in ['a', 'e', 'i', 'o', 'u']:
		print new_word + pyg
	else:
		new_word = word[1:] + first + pyg
		print new_word
else:
	print 'Not an accepted word'
	
	
final = raw_input("Press any key to continue...")