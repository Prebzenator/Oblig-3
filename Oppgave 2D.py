import pandas as pd

# Filbane
filbane = r'C:\Users\prebe\IS-114\Preben-Jensen1\Oblig 3\Oblig-3\Ny mappe\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'
data = pd.read_excel(filbane, sheet_name="KOSandel120000", header=3, names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'], na_values=['.', '..'])

# Beregn gjennomsnittlig prosent fra 2015 til 2023
data['gjennomsnitt'] = data[['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']].mean(axis=1)

# Finn kommunen med lavest gjennomsnitt
lavest_gjennomsnitt = data['gjennomsnitt'].min()
kommuner_med_lavest_gjennomsnitt = data[data['gjennomsnitt'] == lavest_gjennomsnitt]['kom']

# Skriv ut resultatet
print(f"Kommunen(e) med lavest gjennomsnittlig prosent av barn i barnehagen fra 2015 til 2023 er: {kommuner_med_lavest_gjennomsnitt.tolist()} med et gjennomsnitt på {lavest_gjennomsnitt:.1f}%")
