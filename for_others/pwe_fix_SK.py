# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:48:55 2018

@author: calle
"""

import csv

fixed = []
composition = []
composition_fixed = []

with open("/home/calle/Desktop/PWE500_54Fe.csv", "rb") as infile:
    pwe_reader = csv.reader(infile, delimiter = ",")
    next(pwe_reader, None)
    for line in pwe_reader:
        composition = line[4].split(" ")
        composition_fixed = ["C", "", "H", "", "O", "", "N", "", "Fe", "", "S", ""]
        for entry in composition:
            print entry
            if len(entry) > 1:
                if entry[0] == "C":
                    composition_fixed[1] = entry[1:]
                elif entry[0] == "H":
                    composition_fixed[3] = entry[1:]
                elif entry[0] == "O":
                    composition_fixed[5] = entry[1:]
                elif entry[0] == "N":
                    composition_fixed[7] = entry[1:]
                elif entry.startswith("[54]Fe"):
                    if entry.startswith("[54]Fe2"):
                        composition_fixed[9] = entry[6:]
                    else:
                        composition_fixed[9] = "1"
                elif entry[0] == "S":
                    composition_fixed[11] = entry[1:]
            elif not entry[:-1].isdigit():
                if entry == "C":
                    composition_fixed[1] = "1"
                elif entry == "H":
                    composition_fixed[3] = "1"
                elif entry == "O":
                    composition_fixed[5] = "1"
                elif entry == "N":
                    composition_fixed[7] = "1"
                elif entry == "Fe":
                    composition_fixed[9] = "1"
                elif entry == "S":
                    composition_fixed[11] = "1"
        fixed.append(line[:4] + composition_fixed)

with open("/home/calle/Desktop/PWE500_54Fe_fixed.csv", "wb") as outfile:
    csv_output = csv.writer(outfile, delimiter = ",")
    csv_output.writerow(["m/z", "Intensity", "Relative", "Delta (mmu)", "Composition"])
    for line in fixed:
        csv_output.writerow(line)