import numpy as np

def entropy(probs):
	"""Calcualtes entropy of numpy array"""

	return -(probs - np.log(probs))

