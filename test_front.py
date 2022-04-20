import fronts
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# these are ERA5 data I downloaded: change this to whatever temperature, wind and specific humidty data you have
# specific humidity is only needed if you're making fronts on wetbulb temperature
ta=xr.open_dataset('era5_test_data.nc')['t'][0]
ua=xr.open_dataset('era5_test_data.nc')['u'][0]
va=xr.open_dataset('era5_test_data.nc')['v'][0]
hus=xr.open_dataset('era5_test_data.nc')['q'][0]

t_wet=fronts.wetbulb(ta,hus,850,steps=120)

# the threshold and smoothing here I've picked as they work ok with ERA5
# the data is subsetted over a greater range than what's plotting below because of the smoothing - you'll need
# as many extra points outside the region you care about as you have smoothing passes
frontdata=fronts.front(t_wet.loc[0:-72.5,100:200],ua.loc[0:-72.5,100:200],va.loc[0:-72.5,100:200],threshold_i=-1e-10,numsmooth=9)

# plotting the output
clines=frontdata['cold_fronts']
wlines=frontdata['warm_fronts']
slines=frontdata['stationary_fronts']
fig=plt.figure(figsize=(20,10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([110,180,-10,-60])
ax.coastlines()
ax.gridlines()
f=ax.contourf(t_wet.longitude,t_wet.latitude,t_wet,np.arange(250,291,2.5),extend='both',transform=ccrs.PlateCarree(),cmap='RdYlBu_r')
for n in range(len(slines)):
    ax.plot(slines[n][1],slines[n][0],'k',ms=1,transform=ccrs.PlateCarree())
for n in range(len(wlines)):
    ax.plot(wlines[n][1],wlines[n][0],'r',ms=1,transform=ccrs.PlateCarree())
for n in range(len(clines)):
    ax.plot(clines[n][1],clines[n][0],'b',ms=1,transform=ccrs.PlateCarree())
cbar=fig.colorbar(f)
fig.savefig('front_output.pdf')
plt.show()