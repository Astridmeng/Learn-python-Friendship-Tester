#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ageDifCal import getAgeDif
age1 = int(raw_input("insert your age1:"))
age2 = int(raw_input("insert your age2:"))



ageDif=int(getAgeDif(age1,age2))


if ageDif <= 12:
    print("you two can be friends")
else:
    print "opps"

