def get_num_words(book_text):
	word_count = len(book_text.split())
	return word_count

def char_count(text):
	lower_text = text.lower()
	characters = {}
	for char in lower_text:
		if char not in characters:
			characters[char] = 1
		else:
			characters[char] += 1
	return characters

#  returns the number for each character-value pair
def sort_on(items):
	return items["num"]


# Creates a new dictionary for each character and adds to a sorted list

def char_sort(characters):
	dict_list = []
	for item in characters:
		dict = {"char": item, "num": characters[item]}
		dict_list.append(dict)
	dict_list.sort(reverse=True, key=sort_on)
	return (dict_list)

