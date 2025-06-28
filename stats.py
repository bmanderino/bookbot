def get_num_words(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  result = {}
  for letter in text:
    lc = letter.lower()
    if lc in result:
      result[lc] += 1
    else:
      result[lc] = 1

  return result

def sort_on(items):
  return items["num"]

def sorted_dict(dict):
  new_list = []
  for key, value in dict.items():
    if key.isalpha():
      new_list.append({"char": key, "num": value})
  new_list.sort(reverse=True, key=sort_on)
  return new_list