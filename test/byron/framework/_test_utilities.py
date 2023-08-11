#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################|###|#####################################
#  __                            |   |                                    #
# |  |--.--.--.----.-----.-----. |===| This file is part of byron v0.1    #
# |  _  |  |  |   _|  _  |     | |___| An evolutionary optimizer & fuzzer #
# |_____|___  |__| |_____|__|__|  ).(  https://github.com/squillero/byron #
#       |_____|                   \|/                                     #
################################## ' ######################################
# Copyright 2023 Giovanni Squillero and Alberto Tonda
# SPDX-License-Identifier: Apache-2.0

import pytest
from typing import Type

import byron as byron


class MyFrame(byron.classes.FrameABC):
    def __init__(self, parameters=None):
        super().__init__(parameters=parameters)

    @property
    def successors(self):
        return []

    @property
    def name(self):
        return "MyFrame"

    def dump(self, extra_parameters):
        return f"{self.name}({self.parameters})"

    def is_valid(self, obj):
        return True

    def mutate(self, mutation_rate: float) -> Type["byron.classes.EvolvableABC"]:
        pass


class MyMacro(byron.classes.Macro):
    def __init__(self, parameters=None):
        super().__init__(parameters=parameters)

    @property
    def successors(self):
        return []

    @property
    def name(self):
        return "MyMacro"

    def dump(self, extra_parameters):
        return f"{self.name}({self.parameters})"

    def is_valid(self, obj):
        return True

    def mutate(self, mutation_rate: float) -> Type["byron.classes.EvolvableABC"]:
        pass


def test_cook_sequence():
    expected_output = [byron.classes.FrameABC, MyFrame, byron.classes.Macro, MyMacro]
    cooked = byron.f.utilities.cook_sequence([byron.classes.FrameABC, MyFrame, byron.classes.Macro, MyMacro])
    assert cooked == expected_output

    # somelist = [FrameABC, FrameABC]
    # cooked = cook_sequence(somelist)
    # print("smth is cooked")
    # print(cooked)
