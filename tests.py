# Use py.test tests.py to run these unit tests.

import pytest
import math

import babeldix


class TestCircles(object):

    def test_inscribed(self):
        assert babeldix.Circles.is_correct(
            babeldix.Circles.get_answer([[0.5,0.5,0.5]]), 1 - math.pi/4)

    def test_covered(self):
        assert babeldix.Circles.is_correct(
            babeldix.Circles.get_answer([[0.5,0.5,1.0]]), 0)


class TestPlatesScore(object):

    def test_empty(self):
        assert babeldix.Plates.find_solutions('','') == {}

    def test_none(self):
        assert babeldix.Plates.find_solutions('A','b') == {}
        assert babeldix.Plates.find_solutions('A','bbb') == {}
        assert babeldix.Plates.find_solutions('AB','ba') == {}
        assert babeldix.Plates.find_solutions('ABA','abb') == {}
        assert babeldix.Plates.find_solutions('ABA','bba') == {}

    def test_score_zero(self):
        assert babeldix.Plates.find_solutions('A','a') == {'A':0}
        assert babeldix.Plates.find_solutions('AB','ab') == {'AB':0}
        assert babeldix.Plates.find_solutions('ABC','abc') == {'ABC':0}

    def test_score_one(self):
        assert babeldix.Plates.find_solutions('A','ab') == {'Ab':1}
        assert babeldix.Plates.find_solutions('B','ab') == {'aB':1}
        assert babeldix.Plates.find_solutions('AC','abc') == {'AbC':1}
        assert babeldix.Plates.find_solutions('AC','abbc') == {'AbbC':1}
        assert babeldix.Plates.find_solutions('ACD','abcd') == {'AbCD':1}
        assert babeldix.Plates.find_solutions('ABD','abcd') == {'ABcD':1}
        assert babeldix.Plates.find_solutions('BCD','abcd') == {'aBCD':1}
        assert babeldix.Plates.find_solutions('ABC','abcd') == {'ABCd':1}

    def test_score_two(self):
        assert babeldix.Plates.find_solutions('ACE','abcde') == {'AbCdE':2}
        assert babeldix.Plates.find_solutions('BCE','abcde') == {'aBCdE':2}
        assert babeldix.Plates.find_solutions('ACD','abcde') == {'AbCDe':2}

    def test_score_multi_same(self):
        assert babeldix.Plates.find_solutions('ABC','aabc') == {'AaBC':1, 'aABC':1}
        assert babeldix.Plates.find_solutions('ABC','abbc') == {'ABbC':1, 'AbBC':1}
        assert babeldix.Plates.find_solutions('ABC','abcc') == {'ABCc':1, 'ABcC':1}

    def test_score_multi_different(self):
        assert babeldix.Plates.find_solutions('ABC','aaabc') == {'AaaBC':1, 'aAaBC':2, 'aaABC':1}


class TestPlateSolutions(object):

    def test_xyz(self):
        assert babeldix.Plates.get_solutions('XYZ') == {}

    def test_xyy(self):
        assert babeldix.Plates.get_solutions('XYY') == {'XYlYl':2, 'XYlYls':2, 'XYlotomY':1}
