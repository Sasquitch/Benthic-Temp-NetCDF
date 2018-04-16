#Benthic Temperature Data
#David Pasquale
#Davpasquale@gmail.com
#Last edit on 6/15/17
import os
from os.path import isfile, join
#from pandas import read_csv
from netCDF4 import Dataset
import numpy as np
import time

#MUST REMOVE '°' CHARACTER
lat1 = "62 09.514' S" #change to values based on column A B or C
lon1 = "58 28.313' W"

lat2 = "62 09.525' S"
lon2 = "58 28.317' W"

lat3 = "62 09.531' S"
lon3 = "58 28.325' W"

lat4 = "62 09.535' S"
lon4 = "58 28.330' W"

today = time.time()
today = ("File created on: ", time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(today)))
ncFileName = 'Intertidal_Temperature_Data_KGI_C.nc' #Change to B or C depending on the file being worked on
nc = Dataset(ncFileName, 'w', format = 'NETCDF4')

nc.createDimension('time',28966)
nc.createDimension('lat', 1)
nc.createDimension('lon', 1)



time = nc.createVariable('time and date', np.double, 'time')
time.standard_name = 'time'
time.long_name = 'Date and Time [GMT-03:00]'


temp = nc.createVariable('temperature', np.double,'time')
temp.standard_name = 'sea_water_temperature'
temp.units = 'C'
temp.long_name = 'Temperature at given location [C]'

latvar1 = nc.createVariable('latitude location 1', 'f4', 'lat')
latvar1.standard_name = "latitude"
latvar1.units = "degrees_north"
latvar1.axis = "Y"
latvar1.value = lat1

lonvar1 = nc.createVariable('longitude location 1', 'f4', 'lon')
lonvar1.standard_name = "longitude"
lonvar1.units = "degrees_east"
lonvar1.axis = "X"
lonvar1.value = lon1

latvar2 = nc.createVariable('latitude location 2', 'f4', 'lat')
latvar2.standard_name = "latitude"
latvar2.units = "degrees_north"
latvar2.axis = "Y"
latvar2.value = lat2

lonvar2 = nc.createVariable('longitude location 2', 'f4', 'lon')
lonvar2.standard_name = "longitude"
lonvar2.units = "degrees_east"
lonvar2.axis = "X"
lonvar2.value = lon2

latvar3 = nc.createVariable('latitude location 3', 'f4', 'lat')
latvar3.standard_name = "latitude"
latvar3.units = "degrees_north"
latvar3.axis = "Y"
latvar3.value = lat3

lonvar3 = nc.createVariable('longitude location 3', 'f4', 'lon')
lonvar3.standard_name = "longitude"
lonvar3.units = "degrees_east"
lonvar3.axis = "X"
lonvar3.value = lon3

latvar4 = nc.createVariable('latitude location 4', 'f4', 'lat')
latvar4.standard_name = "latitude"
latvar4.units = "degrees_north"
latvar4.axis = "Y"
latvar4.value = lat4


lonvar4 = nc.createVariable('longitude location 4', 'f4', 'lon')
lonvar4.standard_name = "longitude"
lonvar4.units = "degrees_east"
lonvar4.axis = "X"
lonvar4.value = lon4


nc.ncei_template_version = "NCEI_TimeSeries_Orthogonal"

nc.featureType = "TimeSeries"
nc.title = 'temperature collected at the intertidal zone from the area of Polish Polar Station Arctowski in King George Island from 2010-12-07 to 2011-03-18'

nc.conventions = "CF-1.6"
nc.naming_authority = "pl.gda.iopan"
nc.source = "Python script Benthic_Temperature_Data.py"
nc.date_created = today
nc.date_modified = today
nc.creator_name = "Piotr Kuklinski"
nc.creator_email = "kuki@iopan.pl"
nc.creator_url = "http://www.iopan.gda.pl/"
nc.institution = "Polish Academy of Science; Institute of Oceanology (IO PAS)"
nc.project = 'Intertidal temperature data KGI'
nc.publisher_name = "US National Centers for Environmental Information"
nc.publisher_email = "ncei.info@noaa.gov"
nc.publisher_url = "https://www.ncei.noaa.gov"
concat_lat = lat1 + ", " + lat2 + ", " + lat3 + ", " + lat4
nc.latitude = concat_lat
concat_long = lon1 + ", " + lon2 + ", " + lon3 + ", " + lon4
nc.longitude = concat_long
nc.contributor_name = 'Kuklinski Piotr, Balazy Piotr, Institute of Oceanology, Polish Academy of Sciences'
nc.sea_name = 'Southern Sea'
abstract = 'Given the increased glacier retreat,summer melts, sea level rise and ozone losses the intertidal zone is likely to be one of the most rapidly altering of environments but also one of the least investigated in polar waters. This study aims to quantify summer temperature variability in some habitats of the intertidal zone at King George Island. /nThree transects were selected across tidal flat. Four temperature loggers were deployed at each of them from extreme low water spring tide level to extreme high water spring tide level between 07.12.2010 and 18.03.2011. All the loggers were deployed at the rocky substratum. /nIn all the three transects average temperature increased with tidal height. Much higher temperature variability was recorded at higher than at lower tide locations. Differences in temperature between the three study transects existed. /nResults obtained from the studied tidal flat show that several factors combined altogether, including: water movement by tidal forces, wave action, air temperature, sun light intensity, shore lithology and the presence of ice and snow in the area, seem to influence its temperature.'
nc.abstract = abstract
nc.funding = 'Related Funding Agency: Polish Ministry of Science and Higher Education'
nc.platform = 'Polish Polar Station Arctowski'
nc.notes = 'Data Type: temperature (measured); Units: centidegrees Celsius; Observation Type: in situ; Sampling Instrument: logger; Sampling and Analyzing Method: ; Data Quality Information'



nc.close()
