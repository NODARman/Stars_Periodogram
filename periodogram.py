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

# Set the star identifier
myStar = "KIC 004041342"

def Periodogram(star_name=myStar, author="Kepler", quarter=10):
  # Search and download the light curve data
  lc = lk.search_lightcurve(star_name, author=author, quarter=quarter).download()

  search_result = lk.search_lightcurve(star_name, author="Kepler", cadence="long")
  lc_collection = search_result.download_all()

  lc_stitched = lc_collection.stitch()

  # Plot the periodogram
  Per = lc_stitched.normalize(unit='ppm').to_periodogram()
  Period = Per.period.value
  Power = Per.power.value
  MaxPeriod = str(round(Per.period_at_max_power.value, 2))

  for i in range(80):
    Period = np.delete(Period, 0)
    Power = np.delete(Power, 0)

  plt.plot(Period, Power, linewidth=0.5)
  plt.title(str(myStar) +  ', ' + f'P_rot: {MaxPeriod}d')
  plt.show()

Periodogram()
