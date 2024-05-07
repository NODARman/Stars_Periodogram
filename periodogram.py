import matplotlib.pyplot as plt
import lightkurve as lk
import numpy as np

# Set the star identifier
myStar = "KIC 004041342"

def Periodogram(star_name=myStar):
  # Search and download the light curve data
  search_result = lk.search_lightcurve(star_name, author="Kepler", cadence="long")
  lc_collection = search_result.download_all()
  
  # Stitch
  lc_stitched = lc_collection.stitch()

  # Plot the periodogram
  Per = lc_stitched.normalize(unit='ppm').to_periodogram()
  Period = Per.period.value
  Power = Per.power.value
  MaxPeriod = str(round(Per.period_at_max_power.value, 2))

  # Remove unwanted data for visualization
  for i in range(80):
    Period = np.delete(Period, 0)
    Power = np.delete(Power, 0)

  plt.plot(Period, Power, linewidth=0.5)
  plt.title(str(myStar) +  ', ' + f'P_rot: {MaxPeriod}d')
  plt.show()

Periodogram()
