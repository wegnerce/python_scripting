# -*- coding: utf-8 -*-
"""
@author:      Carl-Eric Wegner
@affiliation: Küsel Lab - Aquatic Geomicrobiology
              Friedrich Schiller University of Jena

              carl-eric.wegner@uni-jena.de
"""
# needed modules
import pandas as pd

long = pd.read_csv("/media/cewegner/DATA II/anvio_BC_RNAseq/CL21_COG_annotations_exported.txt", sep="\t")
df = pd.DataFrame(long, columns = ["gene_callers_id", "source", "accession", "function", "e-value"])
df
df.pivot(index="gene_callers_id", columns=["source", "accession", "function", "e-value"])
df
