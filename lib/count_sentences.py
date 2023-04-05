#!/usr/bin/env python3

class MyString:

    def __init__(self,value = ""):
      self._value = value
    
    
    def get_value(self):
      return self._value

    def set_value(self,value):
      if isinstance(value,str):
        self._value = value
      
      else:
        print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
      if "." in self._value:
        return True
      
      else:
        return False

    def is_question(self):
      if "?" in self._value:
        return True
      
      else:
        return False

    def is_exclamation(self):
      if"!" in self._value:
        return True
      
      else:
        return False
    
    def count_sentences(self):
      count = 0
      list = self._value.replace("!",".").replace("?", ".").split(".")
      for i in list:
        if i != "":
          count += 1
      
      return count
      
      
    

string = MyString()
#string.value = "John"
print(string.count_sentences())