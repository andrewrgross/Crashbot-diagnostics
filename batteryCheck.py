### batteryCheck.py -- Andrew Gross -- 2021-09-013
### Check the battery state once a minute. Send out notifications if it gets low.

from time import sleep
from datetime import datetime
#import os
import sys
import subprocess
print('Starting batteryCheck in 30 seconds')
sleep(30)
print('Starting batteryCheck now')
waitCounter = 4

while True:
#	print('Writing battery to ' + sys.argv[1])

	command = 'rostopic echo -n 1 /battery/charge_ratio' # >> test'# + str(sys.argv[1])
	batteryLvl = subprocess.run(command.split(), stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
	batteryData = batteryLvl.stdout.decode('utf-8')
#	print(batteryData)
	if 'ERROR' in batteryData:
		print('The battery node is not running. Ending check loop after '+ waitCounter + ' more failed checks')
		waitCounter = waitCounter -1
		if waitCounter == 0:
			break
	else:
		waitCounter = 4
	batteryData =  round(float(batteryData.split()[1])*100,2)
	output = str(datetime.now().strftime('%a_%b-%d-%Y_%T') + ',' + str(batteryData) + '\n')
	print(output)

	with open('/home/crashbot/Crashbot-diagnostics/batteryLvl.txt', 'a') as f:
		f.write(output)

	sleep(60)
