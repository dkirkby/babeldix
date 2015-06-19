# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

"""Implements the histogram challenge
"""

from __future__ import division, print_function

import random


class Task(object):

    @staticmethod
    def is_correct(response, answer):
        return answer == response


class Hello(Task):

    def get_challenge(self):
        return 'hello'

    @staticmethod
    def get_response(challenge):
        return 'goodbye'

class Histogram(Task):

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


class Circles(Task):

    def __init__(self, min_circles, max_circles):
        self.min_circles = min_circles
        self.max_circles = max_circles

    def get_challenge(self):
        data = []
        num_circles = random.randint(self.min_circles, self.max_circles)
        for i in range(num_circles):
            x,y = random.randint(-1, 17)/16, random.randint(-1, 17)/16
            r = random.randint(2,5)/16
            data.append([x,y,r])
        return data

    @staticmethod
    def get_response(challenge):
        num_darts, num_hits = 100000, 0
        for i in range(num_darts):
            x,y = random.random(), random.random()
            for (xc,yc,r) in challenge:
                d2 = (x - xc)**2 + (y - yc)**2
                if d2 < r**2:
                    num_hits += 1
                    break
        return (num_darts - num_hits)/num_darts

    @staticmethod
    def is_correct(response, answer):
        return abs(response - answer) < 0.01
