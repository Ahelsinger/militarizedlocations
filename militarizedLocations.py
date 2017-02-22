import numpy as np
import pandas as pd
#https://data.world/cow/militarized-dispute-locations
df = pd.read_csv('https://query.data.world/s/2yudmkkzflhmq1bvba4xl4poh')

nameLatLon = (df.loc[:,"mid21location":"longitude"])
lengthOflist = len(df.index)
templengthofList = 100

# PRINTING THE DIFFERENT CELLS
# print df.head()
print df.iloc[0][0],  df.iloc[0][1],  df.iloc[0][2], df.iloc[0][3], df.iloc[0][4]
print
print "df.iloc[0][5]"
print df.iloc[0][5]
print
print "df.iloc[0][6]"
print df.iloc[0][6]
print "LatLon?"
print df.iloc[0][7]
print df.iloc[0][8]

print
print
#try to get all Nan
# print np.where(pd.isnull(df))

nanPlaces = np.where(pd.isnull(df))

#printing the NaN cells
# for i in range(templengthofList):
# 	if nanPlaces:
# 		print nameLatLon.iloc[i][0]

import folium 
map=folium.Map(location=[50.060467, 14.441584],zoom_start=3,tiles='Stamen Terrain')
for i in range(templengthofList):
	theName = df.iloc[i][6]
	theLat = df.iloc[i][7]
	theLon = df.iloc[i][8]
	map.add_child(folium.Marker(location=[(theLat),(theLon)],popup=(theName),icon=folium.Icon(color="blue")))
map.save(outfile='militarizedlocations.html')
# was Makermap0.html

# print dir(map.save)
print
# print help(map.save)
