import pandas as pd
from random import random
from datetime import date, timedelta

def generate_numbers():
	lst = []
	for i in range(1000):
		lst.append(random())
	return pd.DataFrame(lst)

start_date = date.today().replace(day=1, month=1)
day = start_date

for i in range(10):
	for j in range(7):
		filename = 'files/file_' + str(i)  + '_' + str(day) + '.csv'
		df = generate_numbers()
		print (i, day, filename)
		day = day + timedelta(days = 1)
		df.to_csv(filename, sep = ',', header = None, index = None)