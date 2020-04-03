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
    "-f",
    "--fraction_size",
    type=int,
    help="1/fraction of length of file to keep. Int, default is 1000",
    default=1000,
)

args = parser.parse_args()
np.random.seed(args.random_seed)


tweet_IDs = [tweets for tweets in os.listdir(args.path) if tweets.endswith("txt")]
Sampled_tweet_IDs = np.array([])

for tweet_file in tqdm(tweet_IDs):
    with open(args.path + tweet_file, "r") as t:
        tweets = np.array([line.replace("\n", "") for line in t])

    Sampled_tweet_IDs = np.append(
        Sampled_tweet_IDs, np.random.choice(tweets, len(tweets) // args.sample_size)
    )

with open(
    "_".join(
        [args.path + "Random", str(args.sample_size), args.path.replace("/", "-"),]
    )
    + ".txt",
    "w",
) as x:
    for tweetID in Sampled_tweet_IDs:
        x.write(tweetID + "\n")

print("Done!")
