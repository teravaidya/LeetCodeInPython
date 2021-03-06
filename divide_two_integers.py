#!/usr/bin/env python
# encoding: utf-8
"""
divide_two_integers.py

Created by Shengwei on 2014-07-23.
"""

# https://oj.leetcode.com/problems/divide-two-integers/
# tags: medium / hard, signed numbers, bit manipulation, edge cases

"""
Divide two integers without using multiplication, division and mod operator.
"""

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        """A divide operator complying to normal practice in C++ and Java,
        i.e., -5 / 4 == -1, while the result is -2 in Python.
        """
        if divisor == 0:
            raise ValueError('Divisor cannot be 0.')
            
        if abs(dividend) < abs(divisor):
            # including dividend == 0
            return 0
        
        i = 1
        # note: use <= instead of < to reduce loops
        while abs(divisor << i) <= abs(dividend):
            i += 1
        positive = dividend == abs(dividend)
        if positive:
            remainder = dividend - abs(divisor << i - 1)
        else:
            remainder = dividend + abs(divisor << i - 1)
        
        # note: the result from recursive call to self.divide
        #   has sign on it, do not add to count directly!
        count = 2 ** (i - 1)
        if positive ^ (divisor == abs(divisor)):
            return -count + self.divide(remainder, divisor)
        return count + self.divide(remainder, divisor)


class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        """Simplified version: deal with the sign for the first call,
        but only need to handle positive values recusively.
        """
        if divisor == 0:
            raise ValueError('Divisor cannot be 0.')

        # store the sign of the result and only deal with positive
        # values afterward; only the outmost call actually cares about it
        negative = dividend * divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        
        if dividend < divisor:
            # including dividend == 0
            return 0
        
        # note: do not increase divisor directly; it's used recursively
        quotient, accumulator = 1, divisor
        while accumulator << 1 <= dividend:
            accumulator <<= 1
            quotient <<= 1
        remainder = dividend - accumulator
        quotient += self.divide(remainder, divisor)
        
        if negative:
            return -quotient
        return quotient
