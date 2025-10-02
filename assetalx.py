#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asset Allocation Model - employs mean variance optimization where variance is computed using the 
Barra equity risk factor model.

Created on Thu Oct  2 10:29:17 2025

@author: mosesodeiaddai
"""

# cvxpy init
# cvxpy install
# numpy init
# numpy install
import cvxpy as cp
import numpy as np

n = 4

#c represents the objective function(returns) that is being maximized. s is the standform form of the problem 
#and constitutes entries for investment resources and variances. b comprises the constant limits for resources and variance
c= np.array([5000,3000,2100,1500])
s= np.array([[20,50,50,30],[35,22,20,17]])
b = [100,50]

# exposure matrix (4 assets × 2 factors)
X = np.array([
    [1.0, 0.3],
    [0.8, -0.2],
    [1.2, 0.5],
    [0.6, 0.1]
])

# Factor covariance 
Sigma_f = np.array([
    [0.04, 0.01],
    [0.01, 0.03]
])

# Specific variances (asset-specific)
Sigma_eps = np.diag([0.02, 0.025, 0.03, 0.015])

# Full covariance (Barra risk model)
Sigma = X @ Sigma_f @ X.T + Sigma_eps

##

x = cp.Variable(n)
reg = 0.01

obj = cp.Maximize(c @ x - reg * cp.quad_form(x, Sigma))
limits = [s@x<=b,x>=0]

prob = cp.Problem(obj,limits)
prob.solve()

print("Optimal objective:",prob.value)
print("Optimal allocation:",np.round(x.value,2))







