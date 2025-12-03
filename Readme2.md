Tarea 2

<img width="733" height="452" alt="image" src="https://github.com/user-attachments/assets/6988b9b7-4dde-47d6-9d71-4adee5f7488a" />
<img width="714" height="428" alt="image" src="https://github.com/user-attachments/assets/779a0d1f-3b6a-492e-91df-a062277bd8c1" />
<img width="915" height="356" alt="image" src="https://github.com/user-attachments/assets/e0d3d0d0-db20-4b6f-8246-debf587976dc" />

Tarea 3

<img width="942" height="422" alt="image" src="https://github.com/user-attachments/assets/0125374b-ce49-4fc0-ac43-4e4431b03014" />


Tarea 4


import pandas as pd
import os

Archivos = ['Indicadores_Finales', 'Lineas', 'Objetivos', 'Procesos']

for nombre in Archivos:

archivo_csv = f"{nombre}.csv"
archivo_parquet = f"{nombre}.parquet"
   
if os.path.exists(archivo_csv):

try:
            df = pd.read_csv(archivo_csv)
            df.to_parquet(archivo_parquet, index=False)
            print(f"Convertido correctamente: {archivo_csv} -> {archivo_parquet}")         
        except Exception as e:
            print(f"Error al convertir {archivo_csv}: {e}")
else:
        print(f"El archivo no existe en esta carpeta")

Tarea 5


<img width="1470" height="118" alt="image" src="https://github.com/user-attachments/assets/45e88f11-0285-48fd-a50f-57f4b18231d1" />

