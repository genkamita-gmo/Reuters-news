# coding: utf-8
import numpy
from collections import Counter


def discretise_label(list_to_label,bin_list):
    digitized = numpy.digitize(list_to_label, bin_list)
    print "bin: ", str(bin_list),"-> counts of elements after binning:" ounter(digitized).values()
    return digitized - 1
