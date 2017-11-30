import pandas as pd
import numpy as np

class Runner(object):

	def __init__(self, file, search_file):
		self.file = file
		self.search_file = search_file

	def fill_csv(self, compare_cel, compare_id, fill_cel):
		fill_data = pd.read_csv(filepath_or_buffer=self.file, delim_whitespace = False)
		data = fill_data[compare_cel]
		compare_data = pd.read_csv(filepath_or_buffer=self.search_file, delim_whitespace = False)
		dict_data = []
		for row in compare_data:
			# print row[compare_id]
			# print row[fill_cel]
			print row
		# 	dict_data.append({row: compare_data[fill_cel]})
		# print dict_data[0]

runner = Runner('MasterData.csv', 'Products.csv')
runner.fill_csv('RelatedId','ProductId','Name')