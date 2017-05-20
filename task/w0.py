import pandas as pd
from random import random

def generate_numbers():
	lst = []
	for i in range(1000):
		lst.append(random())
	return pd.DataFrame(lst)

# for i in range(10):
# 	df = generate_numbers()
# 	filename = 'files/file_' + str(i) + '.csv'
# 	df.to_csv(filename, sep = ',', header = None, index = None)

from datetime import date
import random

start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().toordinal()
random_day = date.fromordinal(random.randint(start_date, end_date))

print (random_day)
print (type(random_day))