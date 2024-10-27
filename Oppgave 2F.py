import pandas as pd

# Filbane
filbane = r'C:\\Users\\prebe\\IS-114\\Preben-Jensen1\\Oblig 3\\Oblig-3\\Ny mappe\\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'

# Les data fra Excel-filen
data = pd.read_excel(filbane, sheet_name='KOSandel120000', header=3, names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'], na_values=['.', '..'])

# Velg data for året 2020
data_2020 = data[['kom', 'y20']].dropna(subset=['kom'])

# Beregn gjennomsnittlig prosent for alle kommuner for året 2020
gjennomsnitt_2020 = data_2020['y20'].mean()

# Skriv ut data for 2020 og gjennomsnittlig prosent for 2020
print(data_2020)
print(f"Gjennomsnittlig prosent for alle kommuner i 2020: {gjennomsnitt_2020:.2f}%")

