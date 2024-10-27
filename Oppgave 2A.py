import pandas as pd


# Ensure the file path is correct
file_path = r'C:\Users\prebe\IS-114\Preben-Jensen1\Oblig 3\Oblig-3\Ny mappe\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'
kgdata = pd.read_excel(file_path, sheet_name="KOSandel120000",
                           header=3,
                           names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
                           na_values=['.', '..'])

for coln in ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']:
    mask_over_100 = (kgdata[coln] > 100)  # Use df instead of file_path
    kgdata.loc[mask_over_100, coln] = 100.0

kgdata.loc[724:779, 'kom'] = None  # Use df instead of file_path

# Print the modified DataFrame to check the changes
print(kgdata.head())

#Filtrer ut bare navnet på kommunen fra "kom"
#Renser irrelevant data i tabellen
#Input :: SSb-barnehager sheet
#Output :: renset data
def extract_name(x):
    try:
        return x.split(" ")[1] if len(x.split(" ")) > 1 else ""
    except:
        return ""
kgdata["kom"] = kgdata['kom'].apply(extract_name)

#Fjerne ikke-relevante felt
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

#Rensede data
renset_kb = kgdata_no_meta
print(renset_kb)

#Finne kommunen med høyest andel barn til 1-2 år alderen i 2023
høyest = renset_kb['y23'].max()

#Lage en tabell med kommuner som har høyest prosentandel på barnehage
kommune_høyest = renset_kb[renset_kb['y23'] == høyest]

#Skriver ut resultatene
print("Kommuner med høyest andel barn til 1-2 års alderen i 2023:")
print(kommune_høyest[['kom', 'y23']])