#!/usr/bin/env python

# Required imports
import csv

def read_from_input_file(input_filepath):
    """ yields input from file row by row excluding the header row """
    
    with open(input_filepath, "rt", encoding='utf-8') as csvfile:
        filereader = csv.reader(csvfile)
        next(filereader) # excluding the header row 
        for row in filereader:  
            yield row    # reading file row by row at a time


def sort_output_list(output_list):
    """ returns sorted output_list by product (alphabetically) and year (ascending)  """
    
    return sorted(output_list, key=lambda x: (x[0], x[1]))

def write_to_output_file(output_filepath):
    """ writes output_list to output csv file """
    
    with open(output_filepath, "w", newline="", encoding='utf-8') as f:
        writerObj = csv.writer(f)
        writerObj.writerows(output_list_sorted)