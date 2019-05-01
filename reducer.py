#HW4 – Hadoop data Analysis 
#vuduthnh M12483636 NITESH VUDUTHA
#CLOUD COMPUTING HOMEWORK 4

#!/usr/bin/env python
"""Advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

def main(space='\t'):
    # input comes from STDIN (standard input)
    value = read(sys.stdin, space=space)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for this_word, aggregate in groupby(value, itemgetter(0)):
        try:
            count = sum(int(count) for this_word, count in aggregate)
            print "%s%s%d" % (this_word, space, count)
        except ValueError:
            # count was not a number, so silently discard this item
            pass

			
def read(input_file, space='\t'):
    for input_line in input_file:
        yield input_line.rstrip().split(space, 1)			
			

if __name__ == "__main__":
    main()