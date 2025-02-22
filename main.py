from stats import get_num_words, get_num_chars, list_of_dicts
import sys

def get_book_text(file):
	with open(file) as f:
		file_contents = f.read()
	return(file_contents)

def main():
	# I COULDN'T FIGURE OUT HOW TO DO THIS⬇️ 🤦‍♂️️
	if len(sys.argv) == 1:  # so, no book path specified
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)
	else:
		text = get_book_text(sys.argv[1])
	words = text.split()
	num_words = get_num_words(words)
	print(f'Found {num_words} total words')
	# chars = get_num_chars(text)
	# for key, value in chars.items():
	# 	print(f"'{key}': {value}")
	list = list_of_dicts(text)
	for item in list:
		# I COULDNT FIGURE THIS OUT, EITHER!! 🤦‍♂️️
		for char, count in item.items():
			print(f"{char}: {count}")
		
main()
