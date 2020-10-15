#!/usr/bin/env python
"""
Unit tests for Solution strategy class
"""

import unittest
import strategy
import random as r


class TestStrategy(unittest.TestCase):

    def generate_heatmap(self, size, seed):
        r.seed(seed)
        return r.choices(range(0, 256), k=size)

    def generate_solutions(self, heatmap, repeats, seed):
        r.seed(seed)
        return r.choices(range(0, len(heatmap)), heatmap, k=repeats)

    def measure_loss(self, solutions, guesses):
        s = 0
        for i in range(0, len(solutions)):
            s += abs(solutions[i] - guesses[i])
        return s

    def test_synthetic(self):
        heatmap = self.generate_heatmap(50, 20201015)
        solutions = self.generate_solutions(heatmap, 30, 22221100)
        st = strategy.Strategy()
        guesses = st.guess_bars(heatmap, 30)
        self.assertEqual(guesses, [29] * 30)
        self.assertEqual(self.measure_loss(solutions, guesses), 362)




if __name__ == '__main__':
    unittest.main()
