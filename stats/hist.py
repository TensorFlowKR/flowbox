
import gzip
import csv
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt

with gzip.open("../csv_files/2015_group_post.csv.gz", "rb") as f:
  d = csv.reader(f)
  all = np.array(list(d))
  print all[0]

# shares = all[1:,3].astype(np.int, casting="safe") 
likes = all[1:,10].astype(np.int).astype(np.int, casting="safe")
print(likes)

plt.hist(likes, bins=20, range=(0, 100))
plt.title("2015 Likes")
plt.xlabel("Likes")
plt.ylabel("Frequency")
plt.show()