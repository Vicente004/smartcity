Tarea 2

/data_escolar/
├── bronce/                           # Datos tal cual llegan (raw)
│   ├── 2024-2025/
│   │   ├── evaluacion_1/
│   │   │   ├── calificaciones_raw.csv
│   │   │   ├── horas_raw.csv
│   │   │   └── grupos_raw.csv
│   │   ├── evaluacion_2/
│   │   ├── evaluacion_3/
│   │   └── catalogos/                # Datos base del curso
│   │       ├── alumnos_raw.csv
│   │       ├── cursos_raw.csv
│   │       ├── modulos_raw.csv
│   │       └── grupos_raw.csv
│   │
│   └── 2023-2024/                     # Años anteriores (para comparativas)
│       └── ...
│
├── plata/                            # Datos limpios y validados
│   ├── 2024-2025/
│   │   ├── evaluacion_1/
│   │   │   ├── calificaciones_clean.csv
│   │   │   ├── horas_clean.csv
│   │   │   └── grupos_clean.csv
│   │   ├── evaluacion_2/
│   │   ├── evaluacion_3/
│   │   └── catalogos/
│   │       ├── alumnos_clean.csv
│   │       ├── cursos_clean.csv
│   │       ├── modulos_clean.csv
│   │       └── grupos_clean.csv
│   │
│   └── 2023-2024/
│       └── ...
│
└── oro/                              # Datos listos para informes
    ├── comparativas/                 # Datos históricos mezclados
    │   ├── rendimiento_2019-2025.csv
    │   ├── aprobados_2019-2025.csv
    │   └── horas_docencia_2019-2025.csv
    │
    ├── indicadores/                  # Se actualizan 1 vez al año
    │   ├── indicadores_2024-2025.xlsx
    │   ├── indicadores_2023-2024.xlsx
    │   └── serie_historica_indicadores.csv
    │
    └── informes_direccion/
        ├── informe_2024-2025.pdf
        ├── informe_2023-2024.pdf
        └── datos_base_informes.csv

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

