import xbmc, xbmcaddon, time, os

addon_name = 'script.service.site-monitor'
xbmc.log(addon_name + ': Starting site monitor...', xbmc.LOGDEBUG)
while not xbmc.abortRequested:
	server1 = xbmcaddon.Addon().getSetting('server1')
	if server1 != '':
		xbmc.log(addon_name + ': Review ' + server1, xbmc.LOGDEBUG)
		response = os.system('ping -c 1 ' + server1)
		if response == 0:
			xbmc.log(addon_name + ': Up ' + server1, xbmc.LOGDEBUG)
		else:
			xbmc.log(addon_name + ': Down ' + server1, xbmc.LOGDEBUG)
			song = xbmcaddon.Addon().getSetting('song')
			xbmc.Player().play(song)
	time.sleep(60)
