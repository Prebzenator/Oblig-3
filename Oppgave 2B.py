import pandas as pd

# Sørg for at filbanen er korrekt
filbane = r'C:\\Users\\prebe\\IS-114\\Preben-Jensen1\\Oblig 3\\Oblig-3\\Ny mappe\\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'
kgdata = pd.read_excel(filbane, sheet_name="KOSandel120000",
                           header=3,
                           names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
                           na_values=['.', '..'])

for kolonne in ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']:
    mask_over_100 = (kgdata[kolonne] > 100)
    kgdata.loc[mask_over_100, kolonne] = 100.0

kgdata.loc[724:779, 'kom'] = None

# Finn kommunen med den laveste prosentandelen barn i barnehagen i ett- og to-årsalderen i 2023
min_prosent = kgdata['y23'].min()
kommuner_med_min_prosent = kgdata[kgdata['y23'] == min_prosent]['kom']

# Skriv ut resultatet
print(f"Kommunen(e) med den laveste prosentandelen barn i barnehagen i ett- og to-årsalderen i 2023 er: {kommuner_med_min_prosent.tolist()} med en prosentandel på {min_prosent:.1f}%")
