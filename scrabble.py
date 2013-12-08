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
  return

#Boiler plate
if __name__ == '__main__':
  main()
