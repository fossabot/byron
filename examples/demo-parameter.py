# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################################################
#           __________                                                      #
#    __  __/ ____/ __ \__ __   This file is part of byron v4!2.0         #
#   / / / / / __/ /_/ / // /   A versatile evolutionary optimizer & fuzzer  #
#  / /_/ / /_/ / ____/ // /_   https://github.com/microgp/byron          #
#  \__  /\____/_/   /__  __/                                                #
#    /_/ --byron-- /_/      You don't need a big goal, be μ-ambitious!   #
#                                                                           #
#############################################################################
# Copyright 2022-2023 Giovanni Squillero and Alberto Tonda
# SPDX-License-Identifier: Apache-2.0

import byron

# BASIC PARAMETERS

m_int = byron.f.macro(
    "{var} = {num1} {op} {num2}",
    var=byron.f.choice_parameter(["x", "y", "z"]),
    num1=byron.f.integer_parameter(0, 256),
    op=byron.f.choice_parameter(list("+-*")),
    num2=byron.f.integer_parameter(0, 256),
)
m_float = byron.f.macro(
    "{var} = {var} * {num}", var=byron.f.choice_parameter(["x", "y", "z"]), num=byron.f.float_parameter(0, 1)
)
m_array = byron.f.macro("DNA: {dna}", dna=byron.f.array_parameter("CGAT", 42))
macros = [m_int, m_float, m_array]

##block = byron.f.bunch(macros, size=10)
##population = byron.classes.Population(block)
##population += byron.operators.random_individual(population.top_frame)
##individual = population[-1]
##print(f"# {individual!r}")
##print(f"{individual}")
##print()
##print(population.dump_individual(0))
##
##exit(0)

# LOCAL REFERENCE

m_jmp = byron.f.macro("JUMP TO {ref}", ref=byron.f.local_reference())

# block = byron.f.bunch(macros, size=10)
# population = byron.classes.Population(block)
# population += byron.operators.random_individual(population.top_frame)
# individual = population[-1]
# print(f"{individual} ({individual!r})")
# print()
# print(population.dump_individual(0))

# GLOBAL REFERENCE

zap = byron.f.macro("zap!")
subs = byron.f.bunch([zap], size=3, name="whazoo")

# m_outer = byron.f.macro("OUTER JUMP TO {ref}", ref=byron.f.global_reference(target_frame=subs, creative_zeal=1))
m_outer = byron.f.macro("OUTER JUMP TO {ref}", ref=byron.f.global_reference(target_frame="whazoo", creative_zeal=1))
block2 = byron.f.sequence([m_int, m_outer])

population = byron.classes.Population(block2)
population += byron.operators.random_individual(population.top_frame)
individual = population[-1]
print(f"{individual} ({individual!r})")
print()
print(population.dump_individual(0))

individual.as_lgp(filename="demo_parameter-lgp.png", bbox_inches="tight")
individual.as_forest(filename="demo_parameter-forest.png", bbox_inches="tight")

pass
