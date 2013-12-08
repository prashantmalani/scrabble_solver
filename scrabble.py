# scrabble.py
# The main program from where the other routines are called.
# Usage: python scrabble.py <rack of letters>
# Example: python scrabble.py RSTLNE

# Import helper  module
import helper_functions
import sys
helper = helper_functions

def main():
  if len(sys.argv) != 2:
    print 'usage: ./scrabble.py <list of words>'
    exit()
  rack = (sys.argv[1]).upper()
  word_list = helper.get_word_list()
  valid_words = helper.valid_words(word_list, rack)
  valid_word_scores = []
  for word in valid_words:
    score = helper.score_word(word)
    new_tuple = (score, word)
    valid_word_scores.append(new_tuple)
  sorted_valid_scores = sorted(valid_word_scores, reverse=True)
  for pair in sorted_valid_scores:
    print pair[0], pair[1]
  return

#Boiler plate
if __name__ == '__main__':
  main()
