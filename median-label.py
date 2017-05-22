# coding: utf-8
import numpy as np
from operator import itemgetter
import sys

def label_by_median(list_to_label,recursion = 2):
    ''' 
    split list into 4 and clasify them according to the value in the elements
    ''' 

    '''
    Converts a numerical list into a list of discrete labels by recursevily searching for the median and adding a constant to half of the labeled list.
    "recursion" specifies how many times the list is split for the median search and addition of the constant..
    '''

    length = len(list_to_label)
    key_list = range(length)
    label_list = [0] * length
    
    print length
    print list_to_label
    print key_list
    print label_list

    list_to_label, key_list, label_list = [list(x) for x in zip(*sorted(zip(list_to_label, 
                                    key_list, label_list), key=itemgetter(0)))]

    print "----after sorting --------"
    print list_to_label
    print key_list
    print label_list
   
    global_median = length / 2
 #   print global_median
    median_pos_of_lower_half = global_median / 2
    median_pos_of_upper_half = global_median + median_pos_of_lower_half
    
    # the bellow implementation is bad. It only works approximartly correclty for a long enough list.
    label_list[ median_pos_of_lower_half:global_median ] = [1] * (global_median  - median_pos_of_lower_half)
    label_list[ global_median:median_pos_of_upper_half  ] = [2] * (median_pos_of_upper_half + 2 - global_median)
    label_list[ median_pos_of_upper_half:  ] = [3] * (length - median_pos_of_upper_half)

#    print global_median
#    print median_pos_of_lower_half
#    print median_pos_of_upper_half
    print(label_list)
'''
        for index in range(recursion):
            median = np.median(list_to_label)
''' 
    

    print "----after sorting --------"
    print list_to_label
    print key_list
    print label_list

   
    global_median = length / 2
 #   print global_median
    median_pos_of_lower_half = global_median / 2
    median_pos_of_upper_half = global_median + median_pos_of_lower_half
    
    # the bellow implementation is bad. It only works approximartly correclty for a long enough list.
    label_list[ median_pos_of_lower_half:global_median ] = [1] * (global_median  - median_pos_of_lower_half)
    label_list[ global_median:median_pos_of_upper_half  ] = [2] * (median_pos_of_upper_half + 2 - global_median)
    label_list[ median_pos_of_upper_half:  ] = [3] * (length - median_pos_of_upper_half)

if __name__ == "__main__":
    from random import randint
    length = int(sys.argv[1])
    label_by_median([randint(0,100) for _ in xrange(10)]) 
