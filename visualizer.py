import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np


DIR = "CityofWindsorData\\Count\\"
sheets = ["Dorchester Road and Huron Church Road.csv", "Malden Road and Huron Church Road.csv", "Totten Street and Huron Church Road.csv"]


class DataSet:
	def __init__(self):
		self.SBRS = []
		self.WBRS = []
		self.NBRS = []
		self.EBRS = []

		self.SBTS = []
		self.WBTS = []
		self.NBTS = []
		self.EBTS = []

		self.SBLS = []
		self.WBLS = []
		self.NBLS = []
		self.EBLS = []

		self.SBUS = []
		self.WBUS = []
		self.NBUS = []
		self.EBUS = []

		self.SPCWS = []
		self.WPCWS = []
		self.NPCWS = []
		self.EPCWS = []

		self.SPCCWS = []
		self.WPCCWS = []
		self.NPCCWS = []
		self.EPCCWS = []


def startsWithNum(s):
	digset = ("1","2","3","4","5","6","7","8","9","0")
	return s[0] in digset

def getHourly(s):
	index = 0
	hourlySet = []
	print(s)
	while index < len(s) - 4:
		try:
			hourlySet.append(sum([int(s[i]) for i in range(index, index+4)]))
		except ValueError:
			print(s[index])
		index += 4
	return hourlySet

def getDaily(s):
	index = 0
	dailySet = []
	while index < len(s) - 96:
		dailySet.append(sum([int(s[i]) for i in range(index, index+96)]))
		index += 96
	return dailySet



totalData = DataSet()
pedestrianData = DataSet()
bicycleData = DataSet()
workVanData = DataSet()
busData = DataSet()
articulatedTruckData = DataSet()
singleUnitTruckData = DataSet()
# There is 5771 lines per dataset
datasets = [totalData, pedestrianData, bicycleData, workVanData, busData, articulatedTruckData, singleUnitTruckData]

for sheet in sheets:
	lineCount = 0
	times = []
	f = open(DIR + sheet)
	for i in range(7):
		f.readline()

	for i in range(7):

		#Removes additional info from beginning
		for _ in range(4):
			f.readline()

		line = f.readline()

		for _ in range(5771):
			
			# Skip non-data lines at the beginning
			if not startsWithNum(line):
				continue

			# Begin Processing of Data Line	
			try:
				time, SBR, SBT, SBL, SBU, SPCW, SPCCW,  WBR, WBT, WBL, WBU, WPCW, WPCCW, NBR, NBT, NBL, NBU, NPCW, NPCCW, EBR, EBT, EBL, EBU, EPCW, EPCCW = line.split(",")
				times.append(time)

				datasets[i].SBRS.append(SBR)
				datasets[i].WBRS.append(WBR)
				datasets[i].NBRS.append(NBR)
				datasets[i].EBRS.append(EBR)
				
				datasets[i].SBTS.append(SBT)
				datasets[i].WBTS.append(WBT)
				datasets[i].NBTS.append(NBT)
				datasets[i].EBTS.append(EBT)

				datasets[i].SBLS.append(SBL)
				datasets[i].WBLS.append(WBL)
				datasets[i].NBLS.append(NBL)
				datasets[i].EBLS.append(EBL)

				datasets[i].SBUS.append(SBU)
				datasets[i].WBUS.append(WBU)
				datasets[i].NBUS.append(NBU)
				datasets[i].EBUS.append(EBU)
				
				datasets[i].SPCWS.append(SPCW)
				datasets[i].WPCWS.append(WPCW)
				datasets[i].NPCWS.append(NPCW)
				datasets[i].EPCWS.append(EPCW)

				datasets[i].SPCCWS.append(SPCCW)
				datasets[i].WPCCWS.append(WPCCW)
				datasets[i].NPCCWS.append(NPCCW)
				datasets[i].EPCCWS.append(EPCCW)

			
			except ValueError:
				# Chances are we hit a line that had non data information, just print and skip
				print(line)
				pass


'''

	# Just prints how many lines of data there were per sheet
	print(len(SBRS))
	print(len(WBRS))
	print(len(NBRS))
	print(len(EBRS))


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