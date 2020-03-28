import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np

DIR = "CityofWindsorData\\Count\\"
sheets = ["Dorchester Road and Huron Church Road.csv", "Malden Road and Huron Church Road.csv", "Totten Street and Huron Church Road.csv"]


def startsWithNum(s):
	digset = ("1","2","3","4","5","6","7","8","9","0")
	return s[0] in digset

for sheet in sheets:
	lineCount = 0
	NData = []
	EData = []
	SData = []
	WData = []
	times = []
	f = open(DIR + sheet)
	while True:
		line = f.readline()
		if len(line) == 0:
			break

		lineCount += 1
		
		# Skip non-data lines at the beginning
		if not startsWithNum(line):
			pass

		# Begin Processing of Data Line	
		try:
			time, SBR, SBT, SBL, SBU, SPCW, SPCCW,  WBR, WBT, WBL, WBU, WPCW, WPCCW, NBR, NBT, NBL, NBU, NPCW, NPCCW, EBR, EBT, EBL, EBU, EPCW, EPCCW = line.split(",")
			times.append(time)
			SData.append((SBR, SBT, SBL, SBU, SPCW, SPCCW))
			WData.append((WBR, WBT, WBL, WBU, WPCW, WPCCW))
			NData.append((NBR, NBT, NBL, NBU, NPCW, NPCCW))
			EData.append((EBR, EBT, EBL, EBU, EPCW, EPCCW))
		except ValueError:
			# Chances are we hit a line that had non data information, just skip it
			#print(line)
			pass



	SBRS = tuple([s[0] for s in SData])
	WBRS = tuple([s[0] for s in WData])
	NBRS = tuple([s[0] for s in NData])
	EBRS = tuple([s[0] for s in EData])

	# Just prints how many lines of data there were per sheet
	print(len(SBRS))
	print(len(WBRS))
	print(len(NBRS))
	print(len(EBRS))


	'''
	Example code to generate a bar graph and save it as an image
	n_groups = len(SData)
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8

	northRect = plt.bar(index, SBRS, bar_width, alpha=opacity, color='red', label = 'North')
	eastRect = plt.bar(index, WBRS, bar_width, alpha=opacity, color='green', label = 'East')
	southRect = plt.bar(index, NBRS, bar_width, alpha=opacity, color='blue', label = 'South')
	westRect = plt.bar(index, EBRS, bar_width, alpha=opacity, color='yellow', label = 'West')

	plt.ylabel('Traffic')
	plt.xlabel('Time')
	plt.title('Windsor Traffic Data by Time')
	plt.xticks(index + bar_width, tuple(times))
	plt.legend()
	plt.tight_layout()
	plt.show()
	plt.savefig('data1.png')
	'''
#print(SData)