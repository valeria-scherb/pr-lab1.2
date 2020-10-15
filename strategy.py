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
        hd = {}
        i = 0
        for v in hm:
            hd[i] = v
            i += 1
        sm = sorted(hd.items(), key=lambda x: x[1])
        ps = 0
        for it in sm:
            i, p = it
            ps += p
            if ps >= 0.5:
                return [i] * repeats
