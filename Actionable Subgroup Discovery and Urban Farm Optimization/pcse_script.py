import pandas as pd
import os
import pcse
import numpy as np
import time
from datetime import datetime
from pcse.fileinput import CABOFileReader
from pcse.fileinput import YAMLAgroManagementReader
from pcse.fileinput import ExcelWeatherDataProvider
from pcse.fileinput import CSVWeatherDataProvider
from pcse.models import Wofost71_WLP_FD
from pcse.base import ParameterProvider

# function which generates a new recipe using the pcse environment and the array of values passed as parameter and returns the yield of the recipe
def runPcse(array_val, nb_phases, nb_var):

    data_dir = "data/pcse"
    day = pd.date_range(pd.to_datetime('20050101', format = '%Y%m%d'), pd.to_datetime('20051021', format = '%Y%m%d')).tolist()
    len_phase = int(len(day)/nb_phases)
    for i in range(0, nb_var):
        cmpt_p = 0
        for j in range(0, nb_phases):
            cmpt_p += 1
            if cmpt_p == nb_phases:
                arr_data = np.repeat(array_val[i+j*nb_var], len_phase + len(day)%nb_phases)
            else:
                arr_data = np.repeat(array_val[i+j*nb_var], len_phase)
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

        if nb_var == 1:
            irrad = np.repeat(20000, len(day))
            wind = np.repeat(5, len(day))
            tmin = np.repeat(15, len(day))
            tmax = np.repeat(25, len(day))
            vap = np.repeat(1.3, len(day))
            snowdepth = np.repeat(['NaN'], len(day)) 
        elif nb_var == 2:
            wind = np.repeat(5, len(day))
            tmin = np.repeat(15, len(day))
            tmax = np.repeat(25, len(day))
            vap = np.repeat(1.3, len(day))
            snowdepth = np.repeat(['NaN'], len(day)) 
        elif nb_var == 3:
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

    return df_res.iloc[-1].loc['TWSO']
