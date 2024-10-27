import pandas as pd
import altair as alt

# Filbane
filbane = r'C:\Users\prebe\IS-114\Preben-Jensen1\Oblig 3\Oblig-3\Ny mappe\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'
data = pd.read_excel(filbane, sheet_name="KOSandel120000", header=3, names=['Kommune', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'], na_values=['.', '..'])

# Sjekk dataene
print(data.head())

# Velg en kommune (for eksempel Oslo)
kommune = '0301 Oslo'

# Filtrer og smelt dataene for den valgte kommunen
df_kommune = data[data['Kommune'] == kommune].dropna().melt(id_vars=['Kommune'], var_name='År', value_name='Prosent')

# Fjern 'y' fra årstallene og konverter til numerisk
df_kommune['År'] = df_kommune['År'].str[1:].astype(int)

# Lag et diagram med Altair
chart = alt.Chart(df_kommune).mark_line(point=True).encode(
    x='År',
    y='Prosent',
    tooltip=['År', 'Prosent']
).properties(
    title=f'Prosent av barn i ett- og to-årsalderen i barnehagen\nfor {kommune} (2015-2023)',
    width=600,
    height=400
).interactive()

# Lagre diagrammet som HTML
chart.save('chart.html')

print("Diagrammet er lagret som chart.html")
