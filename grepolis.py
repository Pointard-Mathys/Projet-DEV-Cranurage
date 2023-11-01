import math
from subprocess import BELOW_NORMAL_PRIORITY_CLASS
from itertools import product
from scipy.optimize import linprog
import pulp

def can_fit_in_bt(pop_to_insert, bt_pop, bt_capacity, pop_cata):
    nb_bt = math.ceil(pop_cata / bt_capacity)
    pop = pop_to_insert - pop_cata - nb_bt * bt_pop
    if pop < 0:
        return False
    else:
        return True

def bt_count_calculator(total_units_pop, bt_pop, bt_default_capacity, pop_cata):
    transported_pop = 0
    bt_count = 0
    bt_capacity = bt_default_capacity
    if can_fit_in_bt(total_units_pop, bt_pop, bt_default_capacity, pop_cata):
        bt_count += math.ceil(pop_cata / bt_default_capacity)
        transported_cata_pop = pop_cata + bt_count * bt_pop
        bt_capacity += transported_cata_pop % bt_default_capacity
        transported_pop += transported_cata_pop
        total_units_pop -= transported_cata_pop
        while total_units_pop > bt_default_capacity:
            if bt_capacity > 0:
                transported_pop += 1
                bt_capacity -= 1
                total_units_pop -= 1
            else:
                bt_count += 1
                total_units_pop -= bt_pop
                bt_capacity = bt_default_capacity
        return bt_count, bt_capacity
    else:
        return 0, 0

def getIntFromStr(value):
    if value != "":
        count = ""
        for char in value:
            if char.isdigit():
                count += char
        if count != "":
            return int(count)
    return 0