#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:44:26 2019

@author: sequentia7
"""

import pandas as pd
import sys

#python annotate_rna.py mart_export.txt AP_fear_vs_no_fear.txt


mart_export = pd.read_csv(sys.argv[1], sep='\t')
Alias_dict = mart_export.set_index('Gene stable ID')['Gene name'].to_dict()
Description_dict = mart_export.set_index('Gene stable ID')['Gene description'].to_dict()
data = pd.read_csv(sys.argv[2], sep='\t')
data['Alias'] = data['Locus'].map(Alias_dict)
data['Description'] = data['Locus'].map(Description_dict)
up = data[data['log2FC']>0]
down = data[data['log2FC']<0]
up.to_excel('up.xlsx', index=False)
down.to_excel('down.xlsx', index=False)