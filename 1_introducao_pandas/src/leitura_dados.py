"""
author: bernardogoltz
title: leitura do primeiro dataset com pandas 
objetivos:
    - entender a estrutura dos dados
    - verificar valores ausentes
    - colunas categóricas
    - colunas numéricas
"""

import pandas as pd 

df = pd.read_parquet('../data/samp-2025-convencional.parquet')

colunas = df.columns

