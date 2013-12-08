# A list of helper functions to help with the scrabble cheater!
#
# Author: Prashant Malani <p.malani@gmail.com

filename = 'sample_list.txt'

def get_word_list():
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


def valid_words(word_list, rack):
  """ This function takes in the rack of letters, and finds which
  valid words can be created from that list.
  Rack of letters is in STRING form.
  Returns a list of valid words """
  valid_list = []

  # Iterate through every word, and see it can be made from rack
  for word in word_list:
    print word
    valid = True
    used_indices = []
    temp_rack =  list(rack)
    # See if every letter of our word is in the rack.
    # Keep deleting elements found from the rack, to account
    # for repeat letters.
    for i in range(len(word)):
      if word[i] in temp_rack:
        index = temp_rack.index(word[i])
        temp_rack.pop(index)
      else:
        valid = False
        break
    if valid ==  True:
      valid_list.append(word)
  return valid_list
