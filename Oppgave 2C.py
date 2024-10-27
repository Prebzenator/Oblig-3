import pandas as pd

# Ensure the file path is correct
file_path = r'C:\Users\prebe\IS-114\Preben-Jensen1\Oblig 3\Oblig-3\Ny mappe\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'
kgdata = pd.read_excel(file_path, sheet_name="KOSandel120000",
                           header=3,
                           names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
                           na_values=['.', '..'])

for coln in ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']:
    mask_over_100 = (kgdata[coln] > 100)
    kgdata.loc[mask_over_100, coln] = 100.0

kgdata.loc[724:779, 'kom'] = None

# Calculate the average percentage from 2015 to 2023
kgdata['average_percentage'] = kgdata[['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']].mean(axis=1)

# Find the municipality with the highest average percentage
max_average_percentage = kgdata['average_percentage'].max()
municipalities_with_max_average_percentage = kgdata[kgdata['average_percentage'] == max_average_percentage]['kom']

# Print the result
print(f"The municipality(ies) with the highest average percentage of children aged one and two in kindergarten from 2015 to 2023 is/are: {municipalities_with_max_average_percentage.tolist()} with an average percentage of {max_average_percentage:.1f}%")
