# A list of helper functions to help with the scrabble cheater!
#
# Author: Prashant Malani <p.malani@gmail.com


def get_word_list(filename):
  """ This function reads the  input file of words, and outputs
  a list of all the words. We can assume that the file format
  is of one word per line, new-line at the end of each line.
  """
  file = open(filename, 'r')
  word_list = []
  for line in file:
    new_word = line.strip('\n')
    final_word = new_word.strip('\r')
    word_list.append(final_word)
  file.close()
  return word_list
