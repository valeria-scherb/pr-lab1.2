#!/usr/bin/env python
"""
Solution strategy ecognition class
"""

import random as r
import math


class Strategy:
    def normalize(self, heatmap):
        s = sum(heatmap)
        return [a/s for a in heatmap]

    def guess_bars(self, heatmap, repeats):
        hm = self.normalize(heatmap)
        ps = 0
        for i in range(0, len(hm)):
            ps += hm[i]
            if ps >= 0.5:
                return [i] * repeats
