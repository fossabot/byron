# -*- coding: utf-8 -*-
#################################|###|#####################################
#  __                            |   |                                    #
# |  |--.--.--.----.-----.-----. |===| This file is part of Byron v0.1    #
# |  _  |  |  |   _|  _  |     | |___| An evolutionary optimizer & fuzzer #
# |_____|___  |__| |_____|__|__|  ).(  https://github.com/squillero/byron #
#       |_____|                   \|/                                     #
################################## ' ######################################

# Copyright 2023 Giovanni Squillero and Alberto Tonda
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

# =[ HISTORY ]===============================================================
# v1 / April 2023 / Squillero (GX)

__all__ = ["dump_test_individual"]

from byron import rrandom
from byron.sys import *
from byron.global_symbols import *
from byron.classes.selement import SElement
from byron.classes.population import Population


def dump_test_individual(
    top_frame: type[SElement],
    *,
    seed: int | None = 42,
    node_info: bool = True,
    population_extra_parameters: dict | None = None,
    as_lgp: bool = False,
    as_forest: bool = False,
):
    rrandom_state = rrandom.state
    rrandom.seed(seed)
    population_parameters = dict()
    if node_info:
        population_parameters |= {'$dump_node_info': True}
    if population_extra_parameters:
        population_parameters |= population_extra_parameters
    population = Population(top_frame=top_frame, extra_parameters=population_parameters)

    generators = [op for op in get_operators() if op.num_parents is None]
    random_individuals = list()
    while not random_individuals:
        random_individuals = rrandom.choice(generators)(top_frame=top_frame)
    population += random_individuals

    rrandom.state = rrandom_state
    if as_lgp:
        if notebook_mode:
            return population[0].as_lgp()
        else:
            return population[0].as_lgp('test_individual_lgp.svg')
    elif as_forest:
        if notebook_mode:
            return population[0].as_forest()
        else:
            return population[0].as_forest('test_individual_forest.svg')
    else:
        return population.dump_individual(0)
