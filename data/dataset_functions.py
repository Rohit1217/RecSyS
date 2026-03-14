import sys
sys.path.append('..')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


movies=pd.read_csv("../ml1m/movies.dat")
ratings=pd.read_csv("../ml1m/ratings.dat")
users=pd.read_csv("../ml1m/users.dat")

print("OK")