import xbmc, xbmcaddon, xbmcgui, time, os

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__time__ = 5000

line1 = 'Starting site monitor...'
xbmcgui.Dialog().notification(__addonname__, line1, __icon__, __time__)
while not xbmc.abortRequested:
	server1 = __addon__.getSetting('server1')
	if server1 == '':
		continue
	notify = __addon__.getSetting('notify')
	if notify == "true":
		line1 = 'Checking %s ...' % (server1)
		xbmcgui.Dialog().notification(__addonname__, line1, __icon__, __time__)
	response = os.system('ping -c 1 ' + server1)
	if response == 0:
		if notify == "true":
			line1 = '%s is up.' % (server1)
			xbmcgui.Dialog().notification(__addonname__, line1, __icon__, __time__)
	else:
		line1 = '%s is down.' % (server1)
		xbmcgui.Dialog().notification(__addonname__, line1, __icon__, __time__)
		song = __addon__.getSetting('song')
		xbmc.Player().play(song)
	m = int(__addon__.getSetting('check'))
	for i in range(0, m):
		check = int(__addon__.getSetting('check'))
		if m == check:
			time.sleep(60)
		else:
			break
