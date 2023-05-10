#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

p1 = NationalPark("Yosemmette")
p2 = NationalPark("Rocky Mountain")
vis = Visitor("Steeve")
t_1 = Trip(vis, p1, "May 5th", "May 9th")
t_2 = Trip(vis, p1, "May 20th", "May 27th")
t_3 = Trip(vis, p2, "January 5th", "January 20th")

ipdb.set_trace()
