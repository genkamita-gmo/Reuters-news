from __future__ import print_function

import os
import pickle
import sys
import pandas as pd

PYTHON_3 = sys.version_info >= (3, 0)


def read(Return=True):
    for ls in os.listdir('data'):
        if ls.endswith('.pkl'):
            with open('data/' + ls, 'rb') as f:
                list_of_titles = []
                if PYTHON_3:
                    data = pickle.load(f, encoding='latin1')
                else:
                    data = pickle.load(f)
                    if Return is True:
			return data
                for datum in data:
                    print('"' + '{}'.format(datum['title']).replace('"','') + '"')


if __name__ == '__main__':
    read(Return=False)
