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
        if file.endswith(".csv"):  # Nur .csv-Dateien verarbeiten
            output_file_path = os.path.join(input_path, f"{file}")
            # csv_filename = os.path.splitext(relative_path)[0] + ".csv"  # .txt -> .csv
            # print(output_file_path)
            # # Zeige padnas an
            # df = pd.read_csv(output_file_path)
            # print(output_file_path, "+", df.head())

            process_csv(output_file_path)

#dabei die ersten dreie Spalten ignoriert, die jeweiligen Spalten von Spalte 4 bis 10, 11 bis 17, usw. als eine Kategorie angesehen.

def process_csv(input_file):
    category_size = 7  # Anzahl der Spalten pro Kategorie
    start_column = 3  # Spalten-Index ab dem wir starten (Spalte 4 in 0-basierter Indexierung)

    with open(input_file, 'r') as file:
        reader = csv.reader(file)

        for row_number, row in enumerate(reader, start=1):
            if row_number >= 2:
                data = row[3:]

                # Gruppiere die Spalten in Kategorien
                categories = [
                    data[i:i + category_size]
                    for i in range(0, len(data), category_size)
                ]
                # Ausgabe der name encoded Gelenke
                ergebnis = {categorie[0]: index + 1 for index, categorie in enumerate(categories)}
                print(ergebnis)
                # Ausgabe der one hot encoded Gelenke
                ergebnisohe = {v: k for (k, v) in ergebnis.items()}
                print("Categories:", ergebnisohe)


if __name__ == '__main__':
    input_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData_csv'
    # input_file_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData_csv/204_18_5_4_1_chair.csv'
    apply_osp(input_path)