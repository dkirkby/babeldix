# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

"""Implements the histogram challenge
"""

from __future__ import division, print_function

import random


class Hello(object):

	def get_challenge(self):
		return 'hello'

	@staticmethod
	def get_response(challenge):
		return 'goodbye'

class Histogram(object):

	def __init__(self, num_values, bin_size, num_bins):
		self.num_values = num_values
		self.bin_size = bin_size
		self.num_bins = num_bins

	def get_challenge(self):
		max_value = self.num_bins * self.bin_size - 1
		values = [random.randint(0, max_value) for i in range(self.num_values)]
		return [[self.num_bins, self.bin_size], values]

	@staticmethod
	def get_response(challenge):
		num_bins, bin_size = challenge[0][0], challenge[0][1]
		values = challenge[1]
		response = [0]*num_bins
		for value in values:
			response[value//bin_size] += 1
		return response
