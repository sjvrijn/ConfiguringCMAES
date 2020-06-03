#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Config file, containing all hardcoded values such as parallelization settings,
default population sizes and number of ES runs to use for calculating ERT/FCE
values in one clear place.

Nothing else to see here, move along...
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from math import floor
from multiprocessing import cpu_count
from local import MPI_num_host_threads, MPI_num_hosts

__author__ = 'Sander van Rijn <svr003@gmail.com>'

num_threads = 1  # Default case, always true
try:
    num_threads = cpu_count()
    allow_parallel = True if num_threads > 1 else False
except NotImplementedError:
    allow_parallel = False

### General Settings ###
use_MPI = True
MPI_num_total_threads = MPI_num_host_threads * MPI_num_hosts
write_output = True

### ES Settings ###
ES_budget_factor = 1e4  # budget = ndim * ES_budget_factor
ES_num_runs = 5
ES_evaluate_parallel = True

### GA Settings ###
GA_mu = 1               # Assuming a dimensionality of 11
GA_lambda = 12          # (9 boolean + 2 triples)
GA_generations = 20000
GA_budget = GA_lambda * GA_generations
GA_evaluate_parallel = True
GA_num_parallel = int(floor(MPI_num_total_threads / ES_num_runs))

### Experiment Settings ###
default_target = 1e-8
experiment_dims = (2, 3, 5, 10, 20, 40, 15, 25, 30, 35)  # Problem dimensionalities to be tested
experiment_funcs = range(1, 25)                          # BBOB function numbers
