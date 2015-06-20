# -*- coding: utf-8 -*-
# Licensed under a MIT style license - see LICENSE.rst

"""Implements the histogram challenge
"""

from __future__ import division, print_function

import random
import gzip
import re


class Task(object):

    @staticmethod
    def is_correct(response, answer):
        return answer == response


class Hello(Task):

    def get_challenge(self):
        return 'hello'

    @staticmethod
    def get_answer(challenge):
        return 'goodbye'

class Histogram(Task):

    def __init__(self, num_values, min_bin_size, max_bin_size, min_num_bins, max_num_bins):
        self.num_values = num_values
        self.min_bin_size = min_bin_size
        self.max_bin_size = max_bin_size
        self.min_num_bins = min_num_bins
        self.max_num_bins = max_num_bins

    def get_challenge(self):
        num_bins = random.randint(self.min_num_bins, self.max_num_bins)
        bin_size = random.randint(self.min_bin_size, self.max_bin_size)
        max_value = num_bins * bin_size - 1
        values = [random.randint(0, max_value) for i in range(self.num_values)]
        return [[num_bins, bin_size], values]

    @staticmethod
    def get_answer(challenge):
        num_bins, bin_size = challenge[0][0], challenge[0][1]
        values = challenge[1]
        response = [0]*num_bins
        for value in values:
            response[value//bin_size] += 1
        return response


class Circles(Task):

    def __init__(self, min_circles, max_circles):
        assert min_circles <= max_circles, 'min_circles > max_circles'
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
    def get_answer(challenge):
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


class Plates(Task):

    words = set()

    @staticmethod
    def load_words():
        if not Plates.words:
            with gzip.open('wordlist.dat.gz', mode='r') as f:
                for line in f:
                    Plates.words.add(line.strip().lower())
            print('read {} words.'.format(len(Plates.words)))

    def __init__(self, num_letters, min_points):
        assert num_letters > 0, 'num_letters <= 0'
        assert min_points <= 1 + num_letters, 'min points > max points'
        self.num_letters = num_letters
        self.min_points = min_points
        Plates.load_words()

    def get_challenge(self):
        points = None
        while True:
            plate = ''.join([chr(ord('A') + random.randint(0,26)) for i in range(self.num_letters)])
            print('Trying {}'.format(plate))
            answer = Plates.get_answer(plate)
            break
        return plate

    @staticmethod
    def get_score(plate, word, solution='', score=0, solutions={}):
        if plate == '':
            # No more letters to find. Any trailing letters for an extra point?
            if len(word) > 0:
                score += 1
            solutions[solution + word] = score
            return solutions
        # Is the next letter in the remainder of the word?
        next = plate[0].lower()
        if word.count(next) == 0:
            # This branch will not work, so no new solution to add.
            return solutions
        # Find all solutions using the next letter.
        for offset,letter in enumerate(word):
            if letter != next:
                continue
            if offset > 0:
                # Add a point for putting letters before the next letter.
                score += 1
            remainder = word[offset+1:]
            solution = word[:offset] + next.upper() + remainder
            # Recursively look for the next letter in the remainder of the word.
            return Plates.get_score(plate[1:], remainder, solution, score, solutions)

    @staticmethod
    def get_answer(challenge):
        Plates.load_words()
        # Build a regular expression for words that fit this plate.
        plate = challenge.lower()
        regexp = '{letter}' + '{letter}'.join(challenge.lower()) + '{letter}$'
        regexp = re.compile(regexp.format(letter='[a-z]*'))
        candidates = []
        for word in Plates.words:
            if regexp.match(word):
                candidates.append(word)
        if not candidates:
            return []
        return candidates
