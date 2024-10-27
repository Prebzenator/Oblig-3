import pandas as pd

file_path = file_path = r'C:\Users\prebe\IS-114\Preben-Jensen1\Oblig 3\Oblig-3\Ny mappe\ssb-barnehager-2015-2023-alder-1-2-aar.xlsx.xlsx'
df = pd.read_excel(file_path, sheet_name='KOSandel120000', engine='openpyxl')



