# Introduction
This repository provides a method to download and read the data time conversion tables to convert UTC time to UT1 and GPS times.

# Method
The _time_correction_ function permits to download the correction tables (from [UT1](https://maia.usno.navy.mil/products/daily.htm) using the 1976 Precession/1980 Nutation Theory with 90 days of predictions, and [GPS](https://maia.usno.navy.mil/products/leap-second)) under the UNIX operating system (not compatible with others unfortunately), in case the necessary data file is not present in the same directory. Having retrieved the time correction table (either for UT1 or for TAI/GPS), the lines in the file are read and the right information is retrieved. That is:

* For the UT1 convertion, the time correction $\Delta t$ is obtained by mapping the time of the input file (provided in fractional julian date, eg. 2.459907268E+06) to the modified julian dates provided on each line of UT1.txt, giving the date of validity of the correction. To do so, the fraction julian date of the input file is converted to the modified julian date (used by the time correction table), MJD. Flooring MJD provides the same format as the validity date of each line of the UT1.txt conversion table. The floored MJD of the input time is matched to the row having the same validity date, and the $\Delta t$ is retrieved.

* For the GPS convertion, the last row provides the latest $\Delta t$ conversion to be used for active satellites (such as the ones in the context of the assignment). The last row is then selected and the $\Delta t$ obtained. Note that this time difference is the TAI-UTC, this can be converted to GPS time knowning that the TAI is always ahead by 19 s with respect to GPS.

# Inputs
The type of time conversion is specified by either passing type='GPS' or type='UT1' to the function. An input file in CSV format with the first column being the fractional julian date form of the epoch of the orbiting satellite is also given (for the UT1 conversions).

# Working example
