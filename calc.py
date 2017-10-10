#!/usr/bin/env python3.3

import math

def formula(scale, t):
    return t * ((scale * math.exp(-t)) + ((4 - (3 * scale)) * math.exp(-2 * t)) + (((2 * scale) -4) * math.exp(-4 * t)))

def formula_(scale, t):
    return (scale * math.exp(-t)) + ((4 - (3 * scale)) * math.exp(-2 * t)) + (((2 * scale) -4) * math.exp(-4 * t))

def var_formula(scale, t, esperance):
    return ((t - esperance)**2) * formula_(scale, t)

def summ(scale, a, b):
    i = 1
    result = 0
    h = (b - a) / 160

    while (i < 160):
        result += formula(scale, (a + (i * h)))
        i += 1
    return result

def summ_2(scale, a, b):
    i = 0
    result = 0
    h = (b - a) / 160

    while (i < 160):
        result += formula(scale, (a + (i * h) + (h / 2)))
        i += 1
    return result

def var_summ(scale, a, b, esperance):
    i = 1
    result = 0
    h = (b - a) / 160

    while (i < 160):
        result += var_formula(scale, (a + (i * h)), esperance)
        i += 1
    return result

def var_summ2(scale, a, b, esperance):
    i = 0
    result = 0
    h = (b - a) / 160

    while (i < 160):
        result += var_formula(scale, (a + (i * h)) + (h / 2), esperance)
        i += 1
    return result

def summ_normal(scale, a, b, n):
    i = 1
    result = 0
    h = (b - a) / n

    while (i < n):
        result += formula_(scale, (a + (i * h)))
        i += 1
    return result

def summ_normal2(scale, a, b, n):
    i = 0
    result = 0
    h = (b - a) / n

    while (i < n):
        result += formula_(scale, (a + (i * h) + (h / 2)))
        i += 1
    return result

def simpson(a, b, n, scale):
    return ((b - a) / (6 * n)) * (formula(scale, a) + formula(scale, b) + (2 * summ(scale, a, b)) + (4 * summ_2(scale, a, b)))

def var_simpson(a, b, n, scale, esperance):
    return ((b - a) / (6 * n)) * (var_formula(scale, a, esperance) + var_formula(scale, b, esperance) + (2 * var_summ(scale, a, b, esperance)) + (4 * var_summ2(scale, a, b, esperance)))

def simpson_normal(a, b, n, scale):
    return ((b - a) / (6 * n)) * (formula_(scale, a) + formula_(scale, b) + (2 * summ_normal(scale, a, b, n)) + (4 * summ_normal2(scale, a, b, n)))

def calc_average(scale):
    return simpson(0, 16, 160, scale)

def calc_stdev(esperance, scale):
    return math.sqrt(var_simpson(0, 16, 160, scale, esperance))

def fif_percent(scale):
    i = 0.100
    while (simpson_normal(0, i, i * 20, scale) <= 0.5):
        i += 1 / 100
    if (scale == 0.2):
        return i - 1 / 100
    return i

def nin_percent(scale):
    i = 0.100
    while (simpson_normal(0, i, i * 20, scale) <= 0.99):
        i += 1 / 100
    return i

def back_one_minute(scale):
    total_time = simpson_normal(0, 16, 160, scale)
    one_minute = simpson_normal(0, 1, 10, scale)
    return (one_minute / total_time) * 100

def back_two_minutes(scale):
    total_time = simpson_normal(0, 16, 160, scale)
    two_minute = simpson_normal(0, 2, 10, scale)
    return (two_minute / total_time) * 100
