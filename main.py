import sys
from stats import get_num_words
from stats import get_char_count
from stats import sorted_dict

def get_book_text(path):
  with open(path) as f:
    text = f.read()
    return text

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path = sys.argv[1]
  text = get_book_text(path)
  num_words = get_num_words(text)
  num_char = get_char_count(text)
  sorted_list = sorted_dict(num_char)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for items in sorted_list:
    print(f"{items["char"]}: {items["num"]}")
  print("============= END ===============")

main()