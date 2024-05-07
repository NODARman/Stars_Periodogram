from astropy.timeseries import BoxLeastSquares
from astropy.timeseries import LombScargle
from astropy.stats import LombScargle
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from ast import literal_eval
import astropy.units as u
import lightkurve as lk
import pandas as pd
import numpy as np

#excel = pd.read_excel('/content/McQuillan x Santos 1-2 - 89 261 stars - ცალ-ცალკე.xlsx', 'txt')

# Set the star identifier
myStar = "KIC 004041342"

def Periodogram(star_name=myStar, author="Kepler", quarter=10):
  # Search and download the light curve data
  lc = lk.search_lightcurve(star_name, author=author, quarter=quarter).download()

  search_result = lk.search_lightcurve(star_name, author="Kepler", cadence="long")
  lc_collection = search_result.download_all()

  lc_stitched = lc_collection.stitch()
  #lc_stitched.plot()
  #plt.show()

  # ნანების მოშორება და ახალ მასივში შეტანა
  Time=[]
  Flux=[]

  #lc_stitched.plot()
  '''
  for index, item in enumerate(lc_stitched.pdcsap_flux.value):
    if (float(item) != np.nan and float(item) != None and str(item) != '———' and str(item) != '') or (float(lc_stitched.pdcsap_flux[index].value) != np.nan and lc_stitched.pdcsap_flux[index].value != '' and float(lc_stitched.pdcsap_flux[index].value) != None and str(lc_stitched.pdcsap_flux[index].value) != '———'):
      Time.append(float(lc_stitched.time[index].value))
      Flux.append(float(lc_stitched.pdcsap_flux[index].value))

    else:
      pass
      #print(lc_stitched.time[index].value, '------', lc_stitched.pdcsap_flux[index].value)

  Time = np.array(Time)
  Flux = np.array(Flux)'''

  # Plot the periodogram
  Per = lc_stitched.normalize(unit='ppm').to_periodogram()
  Period = Per.period.value
  Power = Per.power.value
  MaxPeriod = str(round(Per.period_at_max_power.value, 2))

  '''
  Per.plot(view='period')
  plt.title('P_rot: ' + str(round(Per.period_at_max_power.value, 2)) + 'days')
  plt.show()
  print(type(Per.period))
  '''
  for i in range(80):
    Period = np.delete(Period, 0)
    Power = np.delete(Power, 0)

  plt.plot(Period, Power, linewidth=0.5)
  plt.title(str(myStar) +  ', ' + f'P_rot: {MaxPeriod}d')
  plt.show()


  '''
  plt.scatter(Time, Flux, s=0.1)
  plt.xlabel('Time')
  plt.ylabel('Flux')
  plt.show()'''

  # Save
  '''
  with open('saved_variables.txt', 'w') as f:
    f.write('stTime\n')
    f.write(str(Time))
    f.write('\n\n')
    f.write('stFlux\n')
    f.write(str(Flux))'''

Periodogram()
