# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:44:30 2020

@author: Nandini Janapati
"""

#import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

DM87 = 18.55  # the distance modulus
DM18 = 30.52

# getting the photometry data for sn1987a


def sn87photometrystats(file, MJDstart, DM):
    file.readline()
    magnitudeV = []
    magnitudeB = []
    magnitudeU = []
    magnitudeUVW2 = []
    magnitudeUVM2 = []
    magnitudeUVW1 = []
    time = []
    for line in file:
        line = line.split(',')
        magnitudeV = magnitudeV + [float(line[7]) - DM]
        magnitudeB = magnitudeB + [float(line[6]) - DM]
        magnitudeU = magnitudeU + [float(line[5]) - DM]
        magnitudeUVW2 = magnitudeUVW2 + [float(line[2]) - DM]
        magnitudeUVM2 = magnitudeUVM2 + [float(line[3]) - DM]
        magnitudeUVW1 = magnitudeUVW1 + [float(line[4]) - DM]
        time = time + [int(float(line[1])) - MJDstart]
    return magnitudeV, magnitudeB, magnitudeU, magnitudeUVW2, magnitudeUVM2, magnitudeUVW1, time

# getting photometry data for SN2018hna, pulled straight from my 'comparing two supernovae code'


def sn18photometrystats(DM, MJDstart, sn):

    time_UVW2 = []  # setting up the variable names for all the things to plot
    mag_UVW2 = []
    time_UVM2 = []
    mag_UVM2 = []
    time_UVW1 = []
    mag_UVW1 = []
    time_U = []
    mag_U = []
    time_B = []
    mag_B = []
    time_V = []
    mag_V = []
# null values will be noted in separate variables to later graph as a scatter plot to cover the points where null values occured.
    time_UVW2null = []
    mag_UVW2null = []
    time_UVM2null = []
    mag_UVM2null = []
    time_UVW1null = []
    mag_UVW1null = []
    time_Unull = []
    mag_Unull = []
    time_Bnull = []
    mag_Bnull = []
    time_Vnull = []
    mag_Vnull = []

    for line in sn:
        line = line.split(" ")
        print(line)
        if line[0] == "UVW2":
            if line[9] != "NULL":
                time_UVW2 += [float(line[5]) - MJDstart]
                mag_UVW2 += [float(line[7]) - DM]
            else:
                time_UVW2null += [float(line[5]) - MJDstart]  # so if the magnitude was null, use the 3 sigma limit value as the magnitude, but also put the date and 3 sigma limit value in separate null variables.
                mag_UVW2null += [float(line[15]) - DM]
                time_UVW2 += [float(line[5]) - MJDstart]
                mag_UVW2 += [float(line[15]) - DM]
        elif line[0] == "UVM2":
            if line[9] != "NULL":
                time_UVM2 += [float(line[5]) - MJDstart]
                mag_UVM2 += [float(line[7]) - DM]
            else:
                time_UVM2null += [float(line[5]) - MJDstart]
                mag_UVM2null += [float(line[15]) - DM]
                time_UVM2 += [float(line[5]) - MJDstart]
                mag_UVM2 += [float(line[15]) - DM]
        elif line[0] == "UVW1":
            if line[9] != "NULL":
                time_UVW1 += [float(line[5]) - MJDstart]
                mag_UVW1 += [float(line[7]) - DM]
            else:
                time_UVW1null += [float(line[5]) - MJDstart]
                mag_UVW1null += [float(line[15]) - DM]
                time_UVW1 += [float(line[5]) - MJDstart]
                mag_UVW1 += [float(line[15]) - DM]
        elif line[0] == "U":
            if line[12] != "NULL":
                time_U += [float(line[8]) - MJDstart]
                mag_U += [float(line[10]) - DM]
            else:
                time_Unull += [float(line[8]) - MJDstart]
                mag_Unull += [float(line[18]) - DM]
                time_U += [float(line[8]) - MJDstart]
                mag_U += [float(line[18]) - DM]
        elif line[0] == "B":
            if line[12] != "NULL":
                time_B += [float(line[8]) - MJDstart]
                mag_B += [float(line[10]) - DM]
            else:
                time_Bnull += [float(line[8]) - MJDstart]
                mag_Bnull += [float(line[18]) - DM]
                time_B += [float(line[8]) - MJDstart]
                mag_B += [float(line[18]) - DM]
        elif line[0] == "V":
            if line[12] != "NULL":
                time_V += [float(line[8]) - MJDstart]
                mag_V += [float(line[10]) - DM]
            else:
                time_Vnull += [float(line[8]) - MJDstart]
                mag_Vnull += [float(line[18]) - DM]
                time_V += [float(line[8]) - MJDstart]
                mag_V += [float(line[18]) - DM]
        else:
            continue

    # created dictionaries for all the variables just so the return command wouldn't get so long.
    normalfilters = {"timeUVW2": time_UVW2, "magUVW2": mag_UVW2, "timeUVM2": time_UVM2, "magUVM2": mag_UVM2, "timeUVW1": time_UVW1, "magUVW1": mag_UVW1, "timeU": time_U, "magU": mag_U, "timeB": time_B, "magB": mag_B, "timeV": time_V, "magV": mag_V}
    nullfilters = {"timeUVW2null": time_UVW2null, "magUVW2null": mag_UVW2null, "timeUVM2null": time_UVM2null, "magUVM2null": mag_UVM2null, "timeUVW1null": time_UVW1null, "magUVW1null": mag_UVW1null, "timeUnull": time_Unull, "magUnull": mag_Unull, "timeBnull": time_Bnull, "magBnull": mag_Bnull, "timeVnull": time_Vnull, "magVnull": mag_Vnull}
    return normalfilters, nullfilters


# getting the explosion date for 87a
MJDstart87 = 46849

# creating the data sets for 87a
sn1987 = open("NEW_SN1987A_photometry.csv", 'r')
magV87, magB87, magU87, magUVW287, magUVM287, magUVW187, time87 = sn87photometrystats(sn1987, MJDstart87, DM87)
sn1987.close()


# getting the explosion date for 18hna
MJDstart18 = 58410.8

# creating the data sets for #18hna
sn2018 = open("SN2018hna_uvotB15.1_(1).dat", 'r')
normalfilters18, nullfilters18 = sn18photometrystats(DM18, MJDstart18, sn2018)
sn2018.close()


# plotting 87a data
plt.figure(1)

plt.plot(time87, magV87, color='green', marker='o', markersize='15')
plt.plot(time87, magB87, color='blue', marker='o', markersize='15')
plt.plot(time87, magU87, color='orange', marker='o', markersize='15')
plt.plot(time87, magUVM287, color='red', marker='o', markersize='15')


# plotting 18hna data
plt.plot(normalfilters18["timeV"], normalfilters18["magV"], color='#71D569', marker='*', markersize='15')  # green
plt.plot(normalfilters18["timeB"], normalfilters18["magB"], color='#698AD5', marker='*', markersize='15')  # blue
plt.plot(normalfilters18["timeU"], normalfilters18["magU"], color='#FABA59', marker='*', markersize='15')  # orange
plt.plot(normalfilters18["timeUVM2"], normalfilters18["magUVM2"], color='#F96689', marker='*', markersize='15')  # pink
plt.scatter(nullfilters18["timeVnull"], nullfilters18["magVnull"], s=600, color='#71D569', marker='v')  # green
plt.scatter(nullfilters18["timeBnull"], nullfilters18["magBnull"], s=600, color='#698AD5', marker='v')  # blue
plt.scatter(nullfilters18["timeUnull"], nullfilters18["magUnull"], s=600, color='#FABA59', marker='v')  # orange
plt.scatter(nullfilters18["timeUVM2null"], nullfilters18["magUVM2null"], s=600, color='#F96689', marker='v')  # pink


# limiting the axes and creating the titles
plt.gca().invert_yaxis()
plt.xlim([0, 20])
plt.ylim([-5, -17])
plt.title("Photometry for SN198A and SN2018hna", fontsize='30')
plt.ylabel('Absolute Magnitude', fontsize='25')
plt.xlabel('Time since Explosion (days)', fontsize='25')
plt.tick_params(labelsize='20')


# setting names for the legend
# SN1987A filter names
sn1987A_vband = mlines.Line2D([], [], color='green', marker='o', markersize=10, label='SN1987A V band')
sn1987A_bband = mlines.Line2D([], [], color='blue', marker='o', markersize=10, label='SN1987A B band')
sn1987A_uband = mlines.Line2D([], [], color='orange', marker='o', markersize=10, label='SN1987A U band')
sn1987A_uvm2band = mlines.Line2D([], [], color='red', marker='o', markersize=10, label='SN1987A UVM2 band')

# SN2018HNA filter names
sn2018hna_vband = mlines.Line2D([], [], color='#71D569', marker='*', markersize=10, label='SN2018hna V band')  # green
sn2018hna_bband = mlines.Line2D([], [], color='#698AD5', marker='*', markersize=10, label='SN2018hna B band')  # blue
sn2018hna_uband = mlines.Line2D([], [], color='#FABA59', marker='*', markersize=10, label='SN2018hna U band')  # orange
sn2018hna_uvm2band = mlines.Line2D([], [], color='#F96689', marker='*', markersize=10, label='SN2018hna UVM2 band')  # pink

# legend
plt.legend(handles=[sn1987A_vband, sn1987A_bband, sn1987A_uband, sn1987A_uvm2band, sn2018hna_vband, sn2018hna_bband, sn2018hna_uband, sn2018hna_uvm2band], fontsize='20')

plt.show()
