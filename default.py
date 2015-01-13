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
while not model.abortRequested():
	model.read()
	server = model.getServer()
	if server == '':
		continue
	check = model.getCheck()
	for i in range(0, check):
		if model.abortRequested():
			break
		if model.hasChanged():
			break
		if i == 0:
			notify = model.getNotify()
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
				song = model.getSong()
				model.play(song)
				sleep = model.getSleep(True)
		time.sleep(sleep)
