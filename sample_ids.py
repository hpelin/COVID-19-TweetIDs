'''

script for rndomly sampling tweetIDs

'''

import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("-r","--random_seed", type=int, help="random seed for sampling. None by default", default=None)
parser.add_argument("-p", "--path", type=str, help="sets the working directory. '.' By default.", default='.')

parser.parse_args()
