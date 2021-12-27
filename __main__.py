#!/usr/bin/env python3

"""

"""

import os
import sys
import argparse
import unittest

class TestBracket(unittest.TestCase):
    def test_checkValidity(self):
        self.assertTrue(checkValidity(good_1))
        self.assertTrue(checkValidity(good_2))
    def test_checkStrangeSymbols(self):
        self.assertFalse(checkValidity(bad_1))
    def test_checkClosingBracket(self):
        self.assertFalse(checkValidity(bad_2))
        self.assertFalse(checkValidity(bad_2_1))
    def test_checkLength(self):
        self.assertFalse(checkValidity(bad_3))
        self.assertFalse(checkValidity(bad_4))
    
def invertInput(i):
    if i == ')':
        return '('
    elif i == ']':
        return '['
    elif i == '}':
        return '{'
    elif i == '(':
        return ')'
    elif i == '[':
        return ']'
    elif i == '{':
        return '}'

def isOpen(char):
    if char == '(' or char == '[' or char == '{':
        return True
    else:
        return False

def isClosed(char):
    if char == ')' or char == ']' or char == '}':
        return True
    else:
        return False
def checkValidity(arr):
    aux = []
    if len(arr) == 0 or len(arr) == 1:
        return False
    else:
        for i in arr:
            if i in ['(','[','{',')',']','}']:
                # Check bracket validity
                if isOpen(i):
                    aux.append(i)
                if isClosed(i):
                    last = invertInput(aux.pop())
                    if i == last:
                        continue
                    else:
                        return False              
            else:
                return False    
        return True
# Create tests inputs

good_1 = ['(','[','{','}',']',')']
good_2 = ['{','[','(',')',']','}']
bad_1 = ['(','b','{','}',']',')','(','[','{','}',']',')']
bad_2 = ['{','[','(',')','[','}','{','[','(',')',']','}']
bad_2_1 = ['{','[','(',')','[','}','{','[','(',')',']','{']
bad_3 = ['']
bad_4 = [')']
unittest.main()


