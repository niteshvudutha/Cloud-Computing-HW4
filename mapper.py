#HW4 – Hadoop data Analysis 
#vuduthnh M12483636 NITESH VUDUTHA
#CLOUD COMPUTING HOMEWORK 4

#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
import sys
import csv


def main(space='\t'):
    # input comes from STDIN (standard input)
    file = input_from_file(sys.stdin)
    for wd in file:
        position=wd[-5:]
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for s_wd in position:
            if s_wd.strip():
                print '%s%s%d' % (s_wd.strip(), space, 1)
            else:
                continue


def input_from_file(file_inp):
    csvreaderinput = csv.reader(file_inp)
    csvreaderinput.next() #Ignoring Headers
    for input_line in csvreaderinput:
        # split the line into words
        yield input_line
				
if __name__ == "__main__":
    main()