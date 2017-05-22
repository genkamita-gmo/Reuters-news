# coding: utf-8
import numpy

def median_label(list_to_label,Bin=5):
    minimum = min(list_to_label)
    maximum = max(list_to_label)
    bins = numpy.linspace(minimum,maximum,Bin)
    digitized = numpy.digitize(list_to_label, bins)
    return digitized
