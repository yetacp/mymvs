#!/usr/bin/python3
import sys
import argparse
import subprocess
import os
import socket
import datetime

"""
Adapted code from https://github.com/dasta400/mvssplitspl
Removed PDF output, sockdev interface
Original code is inside mvsplitspl-origina.zip
"""

countEndJobLine = 0
endJob = False
jobDateDay = ''
jobDateMonth = ''
jobDateYear = ''
jobLines = []
jobMSGCLASS = ''
jobName = ''
jobNumber = ''
jobPrinter = ''
jobProgrammerName = ''
jobRoom = ''
jobTimeAMPM = ''
jobTimeHour = ''
jobTimeMinutes = ''
jobTimeSeconds = ''
jobType = ''
months = ["", "JAN", "FEB", "MAR", "APR", "MAY",
          "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

dirname = os.path.dirname(__file__)
outputdir = os.path.join(dirname, './spool')
infile = os.path.join(dirname, './prt/prt00e.txt')

jobFilenames = []

with open(infile, "r", encoding="utf8", errors='ignore') as prtfile:
    while True:
        line = prtfile.readline()
        if not line:
            break
        if (line[:12] == '****A  START') or (line.find("CONT", 7, 12) > 0):
            jobMSGCLASS = line[4:5]
            jobNumber = line[18:22].strip()
            jobName = line[24:32].strip()
            jobProgrammerName = line[34:55].strip()
            jobRoom = line[61:65].strip()
            jobTimeMinutes = line[70:72]
            jobTimeSeconds = line[73:75]
            jobTimeAMPM = line[76:78]
            jobDateDay = line[79:81]
            jobDateMonth = str(months.index(line[82:85])).zfill(2)
            jobDateYear = line[86:88]
            jobPrinter = line[90:98]
            if line.find("JOB", 14, 17) > 0:
                jobType = 'J'
            elif line.find("STC", 14, 17) > 0:
                jobType = 'S'
            elif line.find("TSU", 14, 17) > 0:
                jobType = 'T'
            jobTimeHour = (str(line[67:69]).strip()).zfill(2)
            hour24 = int(jobTimeHour)
            if jobTimeAMPM == "PM":
                if hour24 < 12:  # convert from 1PM to 11PM, to 13 to 23
                    hour24 = hour24 + 12
            elif hour24 == 12:  # convert 12AM to 00
                hour24 = 0
            jobTimeHour = str(hour24).zfill(2)
        elif line[:11] == '****A   END':
            endJob = True
        jobLines.append(line)
        if endJob:
            yearnow = str(datetime.datetime.now().year)[2:4]
            centurynow = str(datetime.datetime.now().year)[0:2]
            if(int(yearnow) == int(jobDateYear)):
                jobDateYear = str(datetime.datetime.now().year)
            filename = \
                jobDateYear + jobDateMonth + jobDateDay \
                + "_" + jobTimeHour + jobTimeMinutes + jobTimeSeconds \
                + "_" + jobMSGCLASS \
                + "_" + jobPrinter
            filename = filename + "_" + jobType + jobNumber \
                + "_" + jobName
            if not os.path.exists(outputdir):
                try:
                    os.mkdir(outputdir)
                    print("Directory ", outputdir, " created.")
                except OSError as err:
                    print("Directory ", outputdir, " CANNOT be created.")
                    print(err)
                    sys.exit(1)
            filename_prt = outputdir + "/" + filename + ".prt"
            jobFilenames.append(filename_prt)
            with open(filename_prt, "w") as outputfile:
                for line in jobLines:
                    if line != '\f' and line != '\n':
                        outputfile.write(line)
                jobLines.clear()
                endJob = False
                countEndJobLine = 0

total = len(jobFilenames)
if total > 7:
    for i in range(total - 7):
        filename = os.path.join(dirname, './spool', jobFilenames[i])
        os.remove(filename)
