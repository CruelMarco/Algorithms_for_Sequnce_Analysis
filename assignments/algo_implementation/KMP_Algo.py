#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 01:48:17 2025

@author: shaique
"""

# Compute lps table and KMP state transitions for given P and T

def compute_lps(P):
    n = len(P)
    lps = [0] * n
    length = 0  # length of previous longest prefix suffix
    
    for i in range(1, n):
        while length > 0 and P[i] != P[length]:
            length = lps[length - 1]
        if P[i] == P[length]:
            length += 1
            lps[i] = length
        else:
            lps[i] = 0
    return lps

def kmp_states(P, T, lps):
    n, m = len(P), len(T)
    j = 0
    states = []
    for char in T:
        while j > 0 and char != P[j]:
            j = lps[j - 1]
        if char == P[j]:
            j += 1
        states.append(j)
        # do not reset on full match; leave j as is to capture the state=|P|
    return states

# Given data
P = "BBABBBAB"
T = "BBABBBACBBBBABBBAB"

# Compute and display
lps = compute_lps(P)
states = kmp_states(P, T, lps)

print("Pattern P:", P)
print("Text    T:", T)
print("\nlps table:", lps)
print("\nKMP states after each character:")
print(states)
