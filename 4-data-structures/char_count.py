
sentence = input('Please enter a sentence: ')

words = sentence.split(' ')

char_count = {}
for word in words:
	characters = list(word)
	for char in characters:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

sorted_keys = sorted(char_count.keys())
for key in sorted_keys:
	value = char_count[key]
	print("Found:", key, value, "times")
	