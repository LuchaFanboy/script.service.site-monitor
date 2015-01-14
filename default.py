import os, sys, time

try:
	import xbmc, xbmcgui, xbmcaddon

	__cwd__ = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')).decode('utf-8')
	__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib')).decode('utf-8')
	sys.path.append(__resource__)
	from media import *
	model = Model(xbmc, xbmcgui, xbmcaddon)
except ImportError:
	__cwd__ = os.path.dirname(os.path.abspath(__file__)).decode('utf-8')
	__resource__ = os.path.join(__cwd__, 'resources', 'lib').decode('utf-8')
	sys.path.append(__resource__)
	from console import *
	model = Model()

line1 = 'Starting site monitor...'
model.notification(line1)
first = True
while not model.abortRequested():
	if first or model.hasChanged():
		model.read()
		notify = model.getNotify()
		check = model.getCheck()
		count = model.getCount()
		song = model.getSong()
		server = model.getServer()
		first = False
	if server == '':
		continue
	for i in range(0, check):
		if model.abortRequested():
			break
		if model.hasChanged():
			break
		if i == 0:
			if notify == True:
				line1 = 'Checking %s ...' % (server)
				model.notification(line1)
			response = os.system('ping -c 1 ' + server)
			if response == 0:
				if notify == True:
					line1 = '%s is up.' % (server)
					model.notification(line1)
				sleep = model.getSleep(False)
			else:
				line1 = '%s is down.' % (server)
				model.notification(line1)
				count = count - 1
				if count == 0:
					model.play(song)
					count = model.getCount()
				sleep = model.getSleep(True)
		time.sleep(sleep)
