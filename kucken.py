import pandas as pd
import numpy as np
import operator
import csv
import os
import os.path as osp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import os
import csv


def apply_osp(input_path):
    for file in os.listdir(input_path):
        if file.endswith(".csv"):
            end_path = os.path.join(input_path, file)
            # csv_filename = os.path.splitext(relative_path)[0] + ".csv"  # .txt -> .csv
            # print(output_file_path)
            # # Zeige padnas an

            return end_path

#dabei die ersten dreie Spalten ignoriert, die jeweiligen Spalten von Spalte 4 bis 10, 11 bis 17, usw. als eine Kategorie angesehen.

def process_csv(end_path):
    print(f"Eingelesene Datei wird verarbeitet: {end_path}")
    df = pd.read_csv(end_path)
    # df = df[1:] #erste Zeile version irgendwas wird gelöscht
    category_size = 7  # Anzahl der Spalten pro Kategorie
    print(df)

    print(df.columns)

    sad
    # Start ab der zweiten Zeile
    for row_number, row in df.iloc[1:].iterrows():
        # Daten ab Spalte 3
        data = row.iloc[3:].tolist()

        # Gruppiere die Spalten in Kategorien
        categories = [
            data[i:i + category_size]
            for i in range(0, len(data), category_size)
        ]

        # Ausgabe der name-encoded Gelenke
        ergebnis = {categorie[0]: index + 1 for index, categorie in enumerate(categories)}
        print(ergebnis)

        # Ausgabe der one-hot-encoded Gelenke
        ergebnisohe = {v: k for k, v in ergebnis.items()}
        print("Categories:", ergebnisohe)


if __name__ == '__main__':
    input_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData_csv'
    # input_file_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData_csv/204_18_5_4_1_chair.csv'
    df = apply_osp(input_path)
    print("h")
    process_csv(df)
