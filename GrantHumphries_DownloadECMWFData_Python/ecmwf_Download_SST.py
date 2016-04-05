#!/usr/bin/env python

##### Code by Grant Humphries

##### This code will allow users to download SST data from the European Center for Medium range Weather Forecasting (ECMWF)

from ecmwfapi import ECMWFDataServer

# To run this example, you need an API key 
# available from https://api.ecmwf.int/v1/key/
 
server = ECMWFDataServer()

## This will download SST from the ECMWF server

years = range(1979,2013)
for year in years:
    start = str(year)+"0101"
    end = str(year)+"1231"
    i = start+"/to/"+end
    targ = str(year)+"data.nc"

    server.retrieve({
          'dataset' : "interim",
          'step'    : "0",
          #'number'  : "all",
          'levtype' : "sfc",
          'date'    : i,
          'time'    : "12",
          #'origin'  : "all",
          'type'    : "an",
          'format'  : "netcdf",
          'stream'  : "oper",
          ### This is a list of the parameters we want to download - a list of these exist at the ECMWF api website
          'param'   : "134.128/148.128/151.128/164.128/167.128/173.128/186.128/187.128/188.128/206.128/235.128/53.162/55.162/59.162/63.162/64.162/65.162/66.162/69.162/70.162/75.162/81.162/82.162/83.162/84.162/85.162/86.162/87.162/88.162,",
          #'area'    : "70/-130/30/-60",
          'grid'    : "0.75/0.75",
          'target'  : targ
          })



years = range(1979,2013)
for year in years:
    start = str(year)+"0101"
    end = str(year)+"1231"
    i = start+"/to/"+end
    targ = str(year)+"data.nc"

    server.retrieve({
          'dataset' : "interim_full_daily",
          'step'    : "0",
          #'number'  : "all",
          'levtype' : "sfc",
          'date'    : i,
          'time'    : "12",
          #'origin'  : "all",
          'type'    : "an",
          'format'  : "netcdf",
          'stream'  : "wave",
          'param'   : "230.140/232.140,",
          #'area'    : "70/-130/30/-60",
          'grid'    : "0.75/0.75",
          'target'  : targ
          })

    














  

