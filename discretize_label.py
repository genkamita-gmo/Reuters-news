# coding: utf-8
import numpy
from collections import Counter

def discretise_label(list_to_label,Bin=5):
    minimum = min(list_to_label)
    maximum = max(list_to_label)
    bins = numpy.linspace(minimum,maximum,Bin)
    digitized = numpy.digitize(list_to_label, bins)
    print "label value counts: label[0,1,2,3] -> counts ", Counter(digitized).values()    
    return digitized - 1
