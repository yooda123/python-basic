def print_dict(input_dict):
  for k, v in input_dict.items():
    print(f"{k} is {v}")


a = {'ont': 1, 'two': 2}
print(print_dict(a))


def get_first_last_word(text):
  text = text.replace(",", "")
  words = str(text).split()
  return words[0], words[-1]

text = "Hello, My name is Mike."
first, last = get_first_last_word(text)
print(f"first word is '{first}', last one is '{last}'.")