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


def apply_osp(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        if files:
            files = sorted(files)
        for file in files:
            if file.endswith(".csv"):  # Nur .txt-Dateien verarbeiten
                input_file_path = os.path.join(root, file)

                # Ziel-Dateipfad mit .csv-Endung erstellen
                relative_path = os.path.relpath(input_file_path, input_path)
                csv_filename = os.path.splitext(relative_path)[0] + ".csv"  # .txt -> .csv
                output_file_path = os.path.join(output_path, csv_filename)

                # Sicherstellen, dass der Zielordner existiert
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                # Finde alles "untracked" 5, 12, 19 , 25
                # apply_find_untracked(input_file_path)


                # Konvertiere die .txt-Datei in eine .csv-Datei
                apply_txttocsvconvert(input_file_path, output_file_path)
                # Entferne die Zeile "Version 1.0", Entferne die Klammern
                process_txt_file(input_file_path, output_file_path)

"""
def apply_find_untracked(input_file_path):
    # Spaltennummern, die überprüft werden sollen (5, 12, 19, ..., 179)
    columns_to_check = list(range(5, 178, 7))  # Von 5 bis 179, Schrittweite 7

    # Liste für Zeilen, die das Kriterium nicht erfüllen
    issues = []

    with open(input_file_path, 'r') as file:
        reader = csv.reader(file)
        for row_number, row in enumerate(reader, start=1):
            if row_number >= 2:
                # Überprüfen, ob die entsprechenden Spalten vorhanden sind
                for col_index in columns_to_check:
                    if col_index - 1 < len(row):  # Spalte existiert
                        if "Tracked" not in row[col_index - 1]:
                            issues.append((row_number, col_index, row[col_index - 1]))
                    else:
                        issues.append((row_number, col_index, "Spalte fehlt"))

    # Ausgabe der Ergebnisse
    if issues:
        print("", input_file_path)
        print("Untracked gefunden:")
        for issue in issues:
            print(f"Zeile {issue[0]}, Spalte {issue[1]}: {issue[2]}")
    else:
        print("Alle überprüften Spalten enthalten 'Tracked'.")
"""


def apply_txttocsvconvert(input_file_path, output_file_path):
    with open(input_file_path, 'r') as in_file:
        stripped = (line.strip() for line in in_file)  # Leerzeichen entfernen
        lines = (line.split(",") for line in stripped if line)  # Spalten trennen

        # Speichern der CSV-Datei an der gewünschten Stelle
        with open(output_file_path, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('title', 'intro'))  # Optional: Spaltenüberschriften
            writer.writerows(lines)

def process_txt_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Entferne die Zeile "Version 1.0"
    lines = [line for line in lines if not line.strip().startswith("Version 1.0")]

    # Entferne die Klammern "(" und ")"
    processed_lines = [line.replace("(", "").replace(")", "") for line in lines]

    # Schreibe das Ergebnis in die neue Datei
    with open(output_file, 'w') as file:
        file.writelines(processed_lines)


if __name__ == '__main__':
    input_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData/RawData'
    output_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData_csv'
    # input_file_path = 'C:/Users/Boris Grillborzer/PycharmProjects/IntelliRehabDS/SkeletonData_csv/204_18_5_4_1_chair.csv'
    # apply_find_untracked(input_file_path)
    apply_osp(input_path, output_path)