#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 01:48:17 2025

@author: shaique
"""

from collections import defaultdict

def shift_and(P, T): #adapted from slide 21 of 01-2
    masks = defaultdict(int)   # masks[c] == 0 if c not in pattern
    bit = 1
    for c in P:
        masks[c] |= bit
        bit <<= 1
    accept_state = bit >> 1
    D = 0   # bit-mask of active states
    matches = []
    for i, c in enumerate(T):
        D = ((D << 1) | 1) & masks[c]   #update rule: shift left, insert 1, AND with mask, Refer Slide 21 of 01-2
        if D & accept_state:
            matches.append(i - len(P) + 1)
    return matches

def shift_or(P, T):
    m = len(P)
    full = (1 << m) - 1
    # build & invert the masks in one pass
    masks = defaultdict(lambda: full)  
    bit = 1
    for c in P:
        masks[c] &= ~bit   #clear the matching bit (0 = “active” , 1 = "inactive")
        bit <<= 1

    accept_state = bit >> 1
    D = full   #all bits “inactive” (1)
    matches = []
    for i, c in enumerate(T):
        
        D = ((D << 1) | masks[c]) & full   #update rule changed here: shift left, then OR with inverted-mask
        if (D & accept_state) == 0:   #invert acceptance test refer slide 23 of 01-2
            matches.append(i - m + 1)
    return matches

pattern = "ABABC"
text    = "ABABABCCACABAC"

print("Shift-And matches at positions:", shift_and(pattern, text))
print("Shift-Or  matches at positions:", shift_or(pattern, text))
