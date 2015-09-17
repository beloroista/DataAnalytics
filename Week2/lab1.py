import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

pop1940=dict()
pop1950=dict()
pop1960=dict()
pop1970=dict()
pop1980=dict()
pop1990=dict()
pop2000=dict()
pop2010=dict()


try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		pop1940[row[0]]=row[2].replace(',', '')
		pop1950[row[0]]=row[3].replace(',', '')
		pop1960[row[0]]=row[4].replace(',', '')
		pop1970[row[0]]=row[5].replace(',', '')
		pop1980[row[0]]=row[6].replace(',', '')
		pop1990[row[0]]=row[7].replace(',', '')
		pop2000[row[0]]=row[8].replace(',', '')
		pop2010[row[0]]=row[9].replace(',', '')
finally:
	fhand.close()


poptotal = dict()
poptotal[1940]=0
poptotal[1950]=0
poptotal[1960]=0
poptotal[1970]=0
poptotal[1980]=0
poptotal[1990]=0
poptotal[2000]=0
poptotal[2010]=0	
popDifference4050 = dict()	

for key in pop1940:
	poptotal[1940]=poptotal[1940]+int(pop1940[key])	
for key in pop1950:
	poptotal[1950]=poptotal[1950]+int(pop1950[key])
for key in pop1960:
	poptotal[1960]=poptotal[1960]+int(pop1960[key])
for key in pop1970:
	poptotal[1970]=poptotal[1970]+int(pop1970[key])
for key in pop1980:
	poptotal[1980]=poptotal[1980]+int(pop1980[key])
for key in pop1990:
	poptotal[1990]=poptotal[1990]+int(pop1990[key])
for key in pop2000:
	poptotal[2000]=poptotal[2000]+int(pop2000[key])
for key in pop2010:
	poptotal[2010]=poptotal[2010]+int(pop2010[key])


	

	

print "Difference between 1940 - 1950: " + str(poptotal[1950]-poptotal[1940])
print "Difference between 1950 - 1960: " + str(poptotal[1960]-poptotal[1950])
print "Difference between 1960 - 1970: " + str(poptotal[1970]-poptotal[1960])
print "Difference between 1970 - 1980: " + str(poptotal[1980]-poptotal[1970])
print "Difference between 1980 - 1990: " + str(poptotal[1990]-poptotal[1980])
print "Difference between 1990 - 2000: " + str(poptotal[2000]-poptotal[1990])
print "Difference between 2000 - 2010: " + str(poptotal[2010]-poptotal[2000])

#Difference between 1940 - 1950:  5148
#Difference between 1950 - 1960:  -61563
#Difference between 1960 - 1970:  -95088
#Difference between 1970 - 1980:  -96216
#Difference between 1980 - 1990:  -54059
#Difference between 1990 - 2000:  -36352
#Difference between 2000 - 2010:  -27823

print "#Difference between 1940 - 1950 for Mount Washington: " + str(int(pop1950["Mount Washington"])-int(pop1940["Mount Washington"]))
print "#Difference between 1950 - 1960 for Mount Washington: " + str(int(pop1960["Mount Washington"])-int(pop1950["Mount Washington"]))
print "#Difference between 1960 - 1970 for Mount Washington: " + str(int(pop1970["Mount Washington"])-int(pop1960["Mount Washington"]))
print "#Difference between 1970 - 1980 for Mount Washington: " + str(int(pop1980["Mount Washington"])-int(pop1970["Mount Washington"]))
print "#Difference between 1980 - 1990 for Mount Washington: " + str(int(pop1990["Mount Washington"])-int(pop1980["Mount Washington"]))
print "#Difference between 1990 - 2000 for Mount Washington: " + str(int(pop2000["Mount Washington"])-int(pop1990["Mount Washington"]))
print "#Difference between 2000 - 2010 for Mount Washington: " + str(int(pop2010["Mount Washington"])-int(pop2000["Mount Washington"]))
#Difference between 1940 - 1950 for Mount Washington:  -953
#Difference between 1950 - 1960 for Mount Washington:  -1645
#Difference between 1960 - 1970 for Mount Washington:  -2628
#Difference between 1970 - 1980 for Mount Washington:  -2992
#Difference between 1980 - 1990 for Mount Washington:  -1095
#Difference between 1990 - 2000 for Mount Washington:  -822
#Difference between 2000 - 2010 for Mount Washington:  -1079

print "#Difference between 1940 - 1950 for  and bottom: " + str(int(pop1950["North Oakland"])-int(pop1940["North Oakland"]))
print "#Difference between 1950 - 1960 for North Oakland: " + str(int(pop1960["North Oakland"])-int(pop1950["North Oakland"]))
print "#Difference between 1960 - 1970 for North Oakland: " + str(int(pop1970["North Oakland"])-int(pop1960["North Oakland"]))
print "#Difference between 1970 - 1980 for North Oakland: " + str(int(pop1980["North Oakland"])-int(pop1970["North Oakland"]))
print "#Difference between 1980 - 1990 for North Oakland: " + str(int(pop1990["North Oakland"])-int(pop1980["North Oakland"]))
print "#Difference between 1990 - 2000 for North Oakland: " + str(int(pop2000["North Oakland"])-int(pop1990["North Oakland"]))
print "#Difference between 2000 - 2010 for North Oakland: " + str(int(pop2010["North Oakland"])-int(pop2000["North Oakland"]))
#Difference between 1940 - 1950 for North Oakland:  1936
#Difference between 1950 - 1960 for North Oakland:  -610
#Difference between 1960 - 1970 for North Oakland:  1213
#Difference between 1970 - 1980 for North Oakland:  42
#Difference between 1980 - 1990 for North Oakland:  2128
#Difference between 1990 - 2000 for North Oakland:  -979
#Difference between 2000 - 2010 for North Oakland:  694

	
print "#Difference between 1940 - 1950 for Shadyside: " + str(int(pop1950["Shadyside"])-int(pop1940["Shadyside"]))
print "#Difference between 1950 - 1960 for Shadyside: " + str(int(pop1960["Shadyside"])-int(pop1950["Shadyside"]))
print "#Difference between 1960 - 1970 for Shadyside: " + str(int(pop1970["Shadyside"])-int(pop1960["Shadyside"]))
print "#Difference between 1970 - 1980 for Shadyside: " + str(int(pop1980["Shadyside"])-int(pop1970["Shadyside"]))
print "#Difference between 1980 - 1990 for Shadyside: " + str(int(pop1990["Shadyside"])-int(pop1980["Shadyside"]))
print "#Difference between 1990 - 2000 for Shadyside: " + str(int(pop2000["Shadyside"])-int(pop1990["Shadyside"]))
print "#Difference between 2000 - 2010 for Shadyside: " + str(int(pop2010["Shadyside"])-int(pop2000["Shadyside"]))
#Difference between 1940 - 1950 for Shadyside:  1599
#Difference between 1950 - 1960 for Shadyside:  -1102
#Difference between 1960 - 1970 for Shadyside:  -2329
#Difference between 1970 - 1980 for Shadyside:  -1903
#Difference between 1980 - 1990 for Shadyside:  -560
#Difference between 1990 - 2000 for Shadyside:  369
#Difference between 2000 - 2010 for Shadyside:  161

totalDiff20101940 = dict()  
### USE THIS TO SORT, Returns a list (array) ###
for key in pop2010:
	totalDiff20101940[key]=int(pop2010[key])-int(pop1940[key])	
	
print "Top 10 - Worst"
totalDiff20101940 = sorted(totalDiff20101940.items(), key=lambda x:x[1] )
for i in range(10):
	print totalDiff20101940[i]
	
print "Top 10 - Best"	

for i in range(len(totalDiff20101940)-10,len(totalDiff20101940)):
	print totalDiff20101940[i]


	
#Top 10 - Worst

#  ('South Side Flats', -15879)
#  ('Middle Hill', -15322)
#  ('Crawford-Roberts', -14789)
#  ('Bloomfield', -12266)
#  ('Larimer', -11610)
#  ('Mount Washington', -11214)
#  ('East Allegheny', -10835)
#  ('Homewood South', -10678)
#  ('South Side Slopes', -10660)
#  ('Perry South', -10521)
#  ('Homewood North', -10319)
#Top 10 - Best
#  ('Stanton Heights', -9)
#  ('Bon Air', -6)
#  ('Swisshelm Park', 23)
#  ('Oakwood', 290)
#  ('New Homestead', 301)
#  ('Northview Heights', 552)
#  ('Westwood', 618)
#  ('Squirrel Hill North', 928)
#  ('Windgap', 1151)
#  ('Banksville', 2930)
#  ('North Oakland', 4424)
	
