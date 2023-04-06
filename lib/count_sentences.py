#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self._value = value 

  def get_string(self):
    return self._value

  def set_string(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_string, set_string)

  def is_sentence(self):
    if self.value[len(self.value) - 1] == '.':
      return True
    else:
      return False

  def is_question(self):
    if self.value[len(self.value) - 1] == '?':
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value[len(self.value) - 1] == '!':
      return True
    else:
      return False

  def count_sentences(self):
    list_of_strings = self.value.split()
    count = 0
    # print(list_of_strings)
    for letter in list_of_strings:
      if letter[len(letter) - 1] == '.' or letter[len(letter) - 1] == '!' or letter[len(letter) - 1] == '?':
        count += 1

    return count

# my_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
# my_string = MyString("This is a string! It has three sentences. Right?")
# my_string.count_sentences()
