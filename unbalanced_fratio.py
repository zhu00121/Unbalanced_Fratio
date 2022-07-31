# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 15:39:42 2022

@author: Yi Zhu
"""

"""
    Sum of squares of all values from every group combined: ∑x^2
    x is a single value from one group
    SS_total = sum(x^2) - sum(x^2)/n
    
    n = total number of all the values combined (total sample size: ∑nj)
    n = sum(n_j) 
    
    sj = the sum of the values in the jth group
    s_j = sum(x_j)
    
    SS_between = sum(s_j^2/n_j) - (sum(s_j))^2/n
    SS_within = SS - S_between
    
    MS_between = SS_between/df_between = SS_between/(k-1)
    MS_within = SS_within/df_within = SS_within/(n-k)
    k = the number of different groups
    
    F-ratio = MS_between/MS_within
"""

import numpy as np

def f_ratio (g1,g2):
    n1 = g1.size
    n2 = g2.size
    s1 = np.sum(g1)
    s2 = np.sum(g2)
    
    SS_b = np.square(s1)/n1 + np.square(s2/n2) - np.square(s1+s2)/(n1+n2)
    
    SS_total = (np.sum(np.square(g1))+np.sum(np.square(g2)))-np.square(s1+s2)/(n1+n2)
    
    SS_w = SS_total - SS_b
    
    MS_b = SS_b
    MS_w = SS_w/(n1+n2-2)
    
    return MS_b/MS_w