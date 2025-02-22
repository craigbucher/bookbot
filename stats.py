def get_num_words(words):
	return len(words)
	
def get_num_chars(text):
	chars = {}
	text = text.lower()
	for char in text:
		if char not in chars:
			chars[char] = 1
		else:
			chars[char] += 1
	return chars

def sort_on(dict):
    # Get the first (and only) value from the dictionary
    # I COULD NOT FIGURE THIS OUT ON MY OWN !!!!
    return list(dict.values())[0]

def list_of_dicts(text):
	chars = {}
	text = text.lower()
	for char in text:
		if char not in chars:
			chars[char] = 1
		else:
			chars[char] += 1
	list=[]
	for key, value in chars.items():
		if key.isalpha():
			list.append({key:value})
	# Provided in the lesson:
	list.sort(reverse=True, key=sort_on)	
	return list
