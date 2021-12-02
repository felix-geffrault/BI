import pandas as pd

df = pd.read_excel('data/crimes-et-delits-enregistres-par-les-services-de-gendarmerie-et-de-police-depuis-2012.xlsx', sheet_name="Services GN 2012", skiprows=1)

data = df
