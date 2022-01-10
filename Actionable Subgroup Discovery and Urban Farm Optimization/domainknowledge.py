import pandas as pd
import os
import pcse
import numpy as np
import time
import random
from datetime import datetime
from pcse.fileinput import CABOFileReader
from pcse.fileinput import YAMLAgroManagementReader
from pcse.fileinput import ExcelWeatherDataProvider
from pcse.fileinput import CSVWeatherDataProvider
from pcse.models import Wofost71_WLP_FD
from pcse.base import ParameterProvider


def generateExpertRecipe():
    data_dir = "data/pcse"
    arr_irrad = np.array([0,25000,25000])
    arr_rain = np.array([10,10,10])
    arr_wind = np.array([5,5,5])

    for i in range(0, 3):
        if i == 0:
            arr_val = np.array(arr_rain[i])
            arr_val = np.append(arr_val, arr_irrad[i])
            arr_val = np.append(arr_val, arr_wind[i])
        else:
            arr_val = np.append(arr_val, arr_rain[i])
            arr_val = np.append(arr_val, arr_irrad[i])
            arr_val = np.append(arr_val, arr_wind[i])

    day = pd.date_range(pd.to_datetime('20050101', format = '%Y%m%d'), pd.to_datetime('20051021', format = '%Y%m%d')).tolist()
    len_phase = int(len(day)/3)
    for i in range(0, 3):
        cmpt_p = 0
        for j in range(0, 3):
            cmpt_p += 1
            if cmpt_p == 3:
                arr_data = np.repeat(arr_val[i+j*3], len_phase + len(day)%3)
            else:
                arr_data = np.repeat(arr_val[i+j*3], len_phase)
            if j == 0:
                arr_data_var = arr_data.copy()
            else:
                arr_data_var = np.append(arr_data_var, arr_data)
        if i == 0:
            rain = arr_data_var
        elif i == 1:
            irrad = arr_data_var
        elif i == 2:
            wind = arr_data_var

    tmin = np.repeat(15, len(day))
    tmax = np.repeat(25, len(day))
    vap = np.repeat(1.3, len(day))
    snowdepth = np.repeat(['NaN'], len(day))    

    dict_weather = {'DAY': day, 'IRRAD': irrad, 'TMIN': tmin, 'TMAX': tmax, 'VAP': vap, 'WIND': wind, 'RAIN': rain, 'SNOWDEPTH': snowdepth}
    df_weather = pd.DataFrame(dict_weather, columns = ['DAY', 'IRRAD', 'TMIN', 'TMAX', 'VAP', 'WIND', 'RAIN', 'SNOWDEPTH'])
    df_weather['DAY'] = df_weather['DAY'].dt.strftime('%Y%m%d')
    df_weather.to_csv(os.path.join(data_dir, 'df_weather.txt'), index = None, sep = ',')
    filenames = [os.path.join(data_dir,'header.txt'), os.path.join(data_dir, 'df_weather.txt')]

    with open(os.path.join(data_dir, 'weather.csv'), 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())

    cropdata = CABOFileReader(os.path.join(data_dir, 'sug0601.crop'))
    soildata = CABOFileReader(os.path.join(data_dir, 'ec3.soil'))
    sitedata = {'SSMAX'  : 0.,
                    'IFUNRN' : 0,
                    'NOTINF' : 0,
                    'SSI'    : 0,
                    'WAV'    : 100,
                    'SMLIM'  : 0.03,
                    'CO2'    : 360.}

    parameters = ParameterProvider(cropdata = cropdata, soildata = soildata, sitedata = sitedata)
    agromanagement = YAMLAgroManagementReader(os.path.join(data_dir, 'sugarbeet_calendar.amgt'))
    wdp = CSVWeatherDataProvider(os.path.join(data_dir,'weather.csv'))
    wofsim = Wofost71_WLP_FD(parameters, wdp, agromanagement)
    wofsim.run_till_terminate()
    df_res = pd.DataFrame(wofsim.get_output())
    os.remove(os.path.join(data_dir, 'weather.csv'))
    os.remove(os.path.join(data_dir, 'df_weather.txt'))
    
    arr_data = np.append(arr_val, df_res.iloc[-1].loc['TWSO'])
    return(arr_data)
