from util import *

# Add your import statements here
from nltk.tokenize import PunktSentenceTokenizer
import re




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		segmentedText = []
		# List of punctuations where we need to split the text
		punctuations = [';', '\.', '!', '\?']

		# Find all the indices where the text is to be split for sentence segmentation.
		indices = [m.end(0) for m in re.finditer(r'|'.join(punctuations), text)]

		# Split the text into segments using the indices calculated above
		start_index = 0
		stop_index = 0
		for index in indices:
			stop_index = index
			if len(text[start_index:stop_index].strip()) > 0:
				segmentedText.append(text[start_index:stop_index].strip())
			start_index = stop_index

		if len(text[start_index:]) > 0:
			segmentedText.append(text[start_index:].strip())

		return segmentedText


	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		#Fill in code here

		punkt = PunktSentenceTokenizer()
		segmentedText = punkt.tokenize(text)
		
		return segmentedText