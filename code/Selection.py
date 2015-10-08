#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sander van Rijn <svr003@gmail.com>'

"""
This Module contains a collection of Selection operators to be used in the ES-Framework

A Selection operator accepts (mu + lambda) individuals and returns (mu) individuals
that are chosen to be the best of this generation
"""

# import numpy as np


def best(population, new_population, parameters):
    """ Given the population, return the (mu) best """
    if parameters.elitist:
        new_population.extend(population)

    new_population.sort(key=lambda individual: individual.fitness)  # sort descending

    return new_population[:parameters.mu]


def pairwise(population, new_population, parameters):
    """
        Perform a pairwise selection on a population.
        Intended for use with a mirrored sampling strategy to prevent bias.

        Assumes that new_population contains pairs as [P1_a, P1_b, P2_a, P2_b, etc ... ]
    """
    if len(new_population) % 2 != 0:
        raise Exception("Error: attempting to perform pairwise selection on an odd number of individuals")

    # Select the best (=lowest) fitness for each consecutive pair of individuals
    pairwise_filtered = []
    for i in range(len(new_population), step=2):
        if new_population[i].fitness < new_population[i+1].fitness:
            pairwise_filtered.append(new_population[i])
        else:
            pairwise_filtered.append(new_population[i+1])

    # After pairwise filtering, we can re-use the regular selection function
    return best(population, pairwise_filtered, parameters)


def onePlusOneSelection(population, new_population, t, parameters):
    """ (1+1)-selection (with success history) """

    new_individual = new_population[0]
    individual = population[0]

    if new_individual.fitness < individual.fitness:
        parameters.best_fitness = new_individual.fitness
        result = new_population
        parameters.addToSuccessHistory(t, True)
    else:
        result = population
        parameters.addToSuccessHistory(t, False)

    return result


def onePlusOneCholeskySelection(population, new_population, _, parameters):
    """
        (1+1)-selection (with success history)
    """

    new_individual = new_population[0]
    individual = population[0]

    if new_individual.fitness < individual.fitness:
        parameters.best_fitness = new_individual.fitness
        result = new_population
        parameters.lambda_success = True
    else:
        result = population
        parameters.lambda_success = False

    return result


def onePlusOneActiveSelection(population, new_population, _, parameters):
    """
        (1+1)-selection (with success history)
    """

    new_fitness = new_population[0].fitness
    individual = population[0]

    if new_fitness < individual.fitness:
        parameters.best_fitness = new_fitness
        result = new_population
        parameters.lambda_success = True
    else:
        result = population
        parameters.lambda_success = False

    parameters.addToFitnessHistory(new_fitness)

    return result