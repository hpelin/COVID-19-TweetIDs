"""

script for rndomly sampling tweetIDs

"""

import argparse, os
import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser()

parser.add_argument(
    "-r",
    "--random_seed",
    type=int,
    help="random seed for sampling. None by default",
    default=None,
)
parser.add_argument(
    "-p",
    "--path",
    type=str,
    help="sets the working directory. '.' By default.",
    default=".",
)
parser.add_argument(
    "-n",
    "--sample_size",
    type=int,
    help="Sample size per file. Int, default is 10000",
    default=10000,
)

args = parser.parse_args()
np.random.seed(args.random_seed)


tweet_IDs = [tweets for tweets in os.listdir(args.path) if tweets.endswith("txt")]

for tweet_file in tqdm(tweet_IDs):
    with open(args.path + tweet_file, "r") as t:
        tweets = np.array([line.replace("\n", "") for line in t])

    tweets = np.random.choice(tweets, args.sample_size)

    with open(path + "Random_" + str(args.sample_size) + tweet_file, "w") as x:
        for tweetID in tweets:
            x.write(tweetID + "\n")

print("Done!")
