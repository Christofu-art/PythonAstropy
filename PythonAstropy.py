#Import numpy to work with numbers and lists of numbers easily.
import numpy as np

# Import pyplot from matplotlib to help us draw graphs and pictures.
import matplotlib.pyplot as plt

# Import fits from astropy.io to open and use special space picture files called FITS.
from astropy.io import fits

# Import download_file from astropy.utils.data to grab data from the internet without leaving our code.
from astropy.utils.data import download_file

# Import LogStretch and PowerStretch from astropy.visualization to make our space pictures look clearer.
from astropy.visualization import LogStretch, PowerStretch

# Import ImageNormalize from astropy.visualization to help make sure our pictures show up nicely in our graphs.
from astropy.visualization.mpl_normalize import ImageNormalize

#Use This function to download a space image stored in a FITS file
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)
image_file = download_file('https://chandra.harvard.edu/photo/2009/crab/fits/crab.fits', cache=True)
image_file = download_file('https://chandra.harvard.edu/photo/2007/kepler/fits/kepler_300-720eV.fits', cache=True)
image_data = fits.getdata(image_file)

import pprint #"pretty print" module
header = fits.getheader(image_file)
pprint.pprint(header)

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

plt.figure(figsize=(10,10))  # Set the size of the image
plt.imshow(image_data, cmap='coolwarm')
plt.colorbar()
plt.show()