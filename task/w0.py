import pandas as pd
from random import random

def generate_numbers():
	lst = []
	for i in range(1000):
		lst.append(random())
	return pd.DataFrame(lst)

for i in range(10):
	df = generate_numbers()
	filename = 'files/file_' + str(i) + '.csv'
	df.to_csv(filename, sep = ',', header = None, index = None)