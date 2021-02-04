# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:46:59 2020
@author: Nandini Janapati
"""
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
# The two file names you provided:
    # SN2012aw_uvotB15.1.dat
    # SN2018aoz_uvotB15.1.dat
sn1name = 'SN2018hna'  # input("Please enter the name of the first supernova (Ex: 'SN2018hna'): ")
sn2name = 'SN2012aw'  # input("Please enter the name of the second supernova (Ex: 'SN2018hna'): ")

# What you had previously:
    # sn1name = 'SN2018hna'  # input("Please enter the name of the first supernova (Ex: 'SN2018hna'): ")
    # sn2name = 'SN2017fzw'  # input("Please enter the name of the second supernova (Ex: 'SN2018hna'): ")

DM1 = 30.52  # float(input("distance modulus 1: "))
DM2 = 30.52  # float(input("distance modulus 2: "))

MJDstart1 = 58410.8  # float(input("start date 1: "))
MJDstart2 = 58410.8  # float(input("start date 2: "))

# The sn2name wasnt opened so you were comparing the same files
# Also theres no file wi the _(1).dat
sn1 = open(sn1name + "_uvotB15.1.dat", 'r')
sn2 = open(sn2name + "_uvotB15.1.dat", "r")
# What you had previously:
    # sn1 = open(sn1name + "_uvotB15.1_(1).dat", 'r')
    # sn2 = open(sn1name + "_uvotB15.1.dat", "r")


def snphotometrydata(DM, MJDstart, sn):

    time_UVW2 = []
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
                time_UVW2null += [float(line[5]) - MJDstart]
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

    normalfilters = {"timeUVW2": time_UVW2, "magUVW2": mag_UVW2, "timeUVM2": time_UVM2, "magUVM2": mag_UVM2, "timeUVW1": time_UVW1, "magUVW1": mag_UVW1, "timeU": time_U, "magU": mag_U, "timeB": time_B, "magB": mag_B, "timeV": time_V, "magV": mag_V}
    nullfilters = {"timeUVW2null": time_UVW2null, "magUVW2null": mag_UVW2null, "timeUVM2null": time_UVM2null, "magUVM2null": mag_UVM2null, "timeUVW1null": time_UVW1null, "magUVW1null": mag_UVW1null, "timeUnull": time_Unull, "magUnull": mag_Unull, "timeBnull": time_Bnull, "magBnull": mag_Bnull, "timeVnull": time_Vnull, "magVnull": mag_Vnull}
    return normalfilters, nullfilters


normalfilters1, nullfilters1 = snphotometrydata(DM1, MJDstart1, sn1)
sn1.close()
normalfilters2, nullfilters2 = snphotometrydata(DM2, MJDstart2, sn2)
sn2.close()


plt.figure(1)
plt.plot(normalfilters1["timeUVW2"], normalfilters1["magUVW2"], color='black', marker='o', markersize='15')
plt.plot(normalfilters1["timeUVM2"], normalfilters1["magUVM2"], color='red', marker='o', markersize='15')
plt.plot(normalfilters1["timeUVW1"], normalfilters1["magUVW1"], color='purple', marker='o', markersize='15')
plt.plot(normalfilters1["timeU"], normalfilters1["magU"], color='orange', marker='o', markersize='15')
plt.plot(normalfilters1["timeB"], normalfilters1["magB"], color='blue', marker='o', markersize='15')
plt.plot(normalfilters1["timeV"], normalfilters1["magV"], color='green', marker='o', markersize='15')
plt.scatter(nullfilters1["timeUVW2null"], nullfilters1["magUVW2null"], s=600, color='black', marker='v')
plt.scatter(nullfilters1["timeUVM2null"], nullfilters1["magUVM2null"], s=600, color='red', marker='v')
plt.scatter(nullfilters1["timeUVW1null"], nullfilters1["magUVW1null"], s=600, color='purple', marker='v')
plt.scatter(nullfilters1["timeUnull"], nullfilters1["magUnull"], s=600, color='orange', marker='v')
plt.scatter(nullfilters1["timeBnull"], nullfilters1["magBnull"], s=600, color='blue', marker='v')
plt.scatter(nullfilters1["timeVnull"], nullfilters1["magVnull"], s=600, color='green', marker='v')

plt.plot(normalfilters2["timeUVW2"], normalfilters2["magUVW2"], color='#ababab', marker='*', markersize='15')
plt.plot(normalfilters2["timeUVM2"], normalfilters2["magUVM2"], color='#f59fa6', marker='*', markersize='15')
plt.plot(normalfilters2["timeUVW1"], normalfilters2["magUVW1"], color='#b991cc', marker='*', markersize='15')
plt.plot(normalfilters2["timeU"], normalfilters2["magU"], color='#e8a561', marker='*', markersize='15')
plt.plot(normalfilters2["timeB"], normalfilters2["magB"], color='#95d8e6', marker='*', markersize='15')
plt.plot(normalfilters2["timeV"], normalfilters2["magV"], color='#9ccc54', marker='*', markersize='15')
plt.scatter(nullfilters2["timeUVW2null"], nullfilters2["magUVW2null"], s=600, color='#ababab', marker='v')
plt.scatter(nullfilters2["timeUVM2null"], nullfilters2["magUVM2null"], s=600, color='#f59fa6', marker='v')
plt.scatter(nullfilters2["timeUVW1null"], nullfilters2["magUVW1null"], s=600, color='#b991cc', marker='v')
plt.scatter(nullfilters2["timeUnull"], nullfilters2["magUnull"], s=600, color='#e8a561', marker='v')
plt.scatter(nullfilters2["timeBnull"], nullfilters2["magBnull"], s=600, color='#95d8e6', marker='v')
plt.scatter(nullfilters2["timeVnull"], nullfilters2["magVnull"], s=600, color='#9ccc54', marker='v')
plt.gca().invert_yaxis()

sn1_uvw2band = mlines.Line2D([], [], color='black', marker='o', markersize=10, label=sn1name + ' UVW2 band')
sn1_uvm2band = mlines.Line2D([], [], color='red', marker='o', markersize=10, label=sn1name + ' UVM2 band')
sn1_uvw1band = mlines.Line2D([], [], color='purple', marker='o', markersize=10, label=sn1name + ' UVW1 band')
sn1_uband = mlines.Line2D([], [], color='orange', marker='o', markersize=10, label=sn1name + ' U band')
sn1_bband = mlines.Line2D([], [], color='blue', marker='o', markersize=10, label=sn1name + ' B band')
sn1_vband = mlines.Line2D([], [], color='green', marker='o', markersize=10, label=sn1name + ' V band')

sn2_uvw2band = mlines.Line2D([], [], color='#ababab', marker='*', markersize=10, label=sn2name + ' UVW2 band')
sn2_uvm2band = mlines.Line2D([], [], color='#f59fa6', marker='*', markersize=10, label=sn2name + ' UVM2 band')
sn2_uvw1band = mlines.Line2D([], [], color='#b991cc', marker='*', markersize=10, label=sn2name + ' UVW1 band')
sn2_uband = mlines.Line2D([], [], color='#e8a561', marker='*', markersize=10, label=sn2name + ' U band')
sn2_bband = mlines.Line2D([], [], color='#95d8e6', marker='*', markersize=10, label=sn2name + ' B band')
sn2_vband = mlines.Line2D([], [], color='#9ccc54', marker='*', markersize=10, label=sn2name + ' V band')

plt.legend(handles=[sn1_uvw2band, sn1_uvm2band, sn1_uvw1band, sn1_uband, sn1_bband, sn1_vband, sn2_uvw2band, sn2_uvm2band, sn2_uvw1band, sn2_uband, sn2_bband, sn2_vband], fontsize='20')
plt.show()