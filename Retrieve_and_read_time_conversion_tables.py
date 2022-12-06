import numpy as np
import csv
import os
import time

def read_CSV(file):
    with open(file, 'r') as file:
        csvreader = csv.reader(file)
        csv_headings = next(csvreader)
        first_line = next(csvreader)
        first_line = [float(i) for i in first_line]
        data = np.array(first_line)
        for row in csvreader:
            row = [float(i) for i in row]
            data = np.vstack((data, row))
    return data

def time_correction(input_file, type='UT1'):
    # Check which files we have
    orbit_data = read_CSV(input_file)
    JD = orbit_data[:, 0]; MJD = JD - 2400000.5
    MJD_floored = np.floor(MJD)
    entries = os.listdir('./')  # Obtain files in directory
    if type == 'UT1':
        # Download file
        if 'UT1.txt' in entries:
            pass  # do nothing
        else:
            PATH = "https://maia.usno.navy.mil/ser7/finals.daily"
            os.system(f"curl -o './UT1.txt' '{PATH}'")
            time.sleep(0.1)
        # Get data
        with open('./UT1.txt', "r") as text_file:
            fin = text_file.readlines()
            jd_fin = [float(fin[i][7:14]) for i in range(0, len(fin)-1)]  # Not so efficient, investigate something different
            delta = [float(fin[jd_fin.index(MJD_floored[i])][58:68]) for i in range(0, len(MJD))]
        ## Implement the time conversion here ##
    elif type == 'GPS':
        if 'GPS.txt' in entries:
            pass  # do nothing
        else:
            PATH = "https://maia.usno.navy.mil/ser7/tai-utc.dat"
            os.system(f"curl -o './GPS.txt' '{PATH}'")
            time.sleep(0.1)
        with open('./GPS.txt', "r") as text_file:
            fin = text_file.readlines()
            Delta_TAI = float(fin[-1][37:40])
        ## Implement the time conversion here ##

    else:
        print("Type conversion not supported")
        exit()
