from stats import get_num_words, char_count, char_sort

import sys

def main():
	if not len(sys.argv) == 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else: 
		book_path = sys.argv[1]
		book_text = (get_book_text(book_path))
		word_count = get_num_words(book_text)
		character_count = char_count(book_text)
		print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
		print("----------- Word Count ----------")
		print(f"Found {word_count} total words")
		print("--------- Character Count -------")
		for i in char_sort(character_count):
			if i["char"].isalpha():
				print(f"{i['char']}: {i['num']}")

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

main()
