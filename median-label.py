# coding: utf-8
import numpy
import sys
sys.argv[1]

def median_label(list_to_label,Bin=5):
    maximum = max(list_to_label)
    bins = numpy.linspace(0,maximum,Bin)
    digitized = numpy.digitize(data, bins)
    return digitized
