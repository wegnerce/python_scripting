import csv

txt_in = "/home/calle/Desktop/summary.txt" # path to your input file
txt_out = "/home/calle/Desktop/summary_fixed.txt" # path to output file

fixed = []

with open(txt_in, "rb") as infile:
    gen_reader = csv.reader(infile, delimiter = " ")
    for line in gen_reader:
        line[1] = " ".join(line[1:])
        fixed.append(line)

with open(txt_out, "wb") as outfile:
    gen_writer = csv.writer(outfile, delimiter = ",")
    gen_writer.writerows(fixed)

