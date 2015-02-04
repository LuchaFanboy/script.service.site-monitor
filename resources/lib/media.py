import serial, time;

class Model(object):
	def __init__(self, xbmc, xbmcgui, xbmcaddon):
		self._xbmc = xbmc
		self._xbmcgui = xbmcgui
		self._xbmcaddon = xbmcaddon.Addon()
		self._addonname = self._xbmcaddon.getAddonInfo('name')
		self._icon = self._xbmcaddon.getAddonInfo('icon')
		self._time = 5000
		self._arduino = False

	def notification(self, line1):
		self._xbmcgui.Dialog().notification(self._addonname, line1, self._icon, self._time)

	def abortRequested(self):
		return self._xbmc.abortRequested

	def read(self):
		self._notify = (self._xbmcaddon.getSetting('notify') == 'true')
		self._check = int(self._xbmcaddon.getSetting('check'))
		self._count = int(self._xbmcaddon.getSetting('count'))
		self._song = self._xbmcaddon.getSetting('song')
		self._server = self._xbmcaddon.getSetting('server1')

	def hasChanged(self):
		notify = (self._xbmcaddon.getSetting('notify') == 'true')
		if self._notify != notify:
			return True
		check = int(self._xbmcaddon.getSetting('check'))
		if self._check != check:
			return True
		count = int(self._xbmcaddon.getSetting('count'))
		if self._count != count:
			return True
		song = self._xbmcaddon.getSetting('song')
		if self._song != song:
			return True
		server = self._xbmcaddon.getSetting('server1')
		if self._server != server:
			return True
		return False

	def getNotify(self):
		return self._notify;

	def getCheck(self):
		return self._check

	def getCount(self):
		return self._count

	def getSong(self):
		return self._song

	def getServer(self):
		return self._server

	def play(self, song):
		if self._arduino == False:
			try:
				ser = serial.Serial('/dev/arduino', 9600)
				time.sleep(2)
				ser.write(b'0')
				ser.close()
				self._arduino = True
			except:
				pass
		self._xbmc.Player().play(song)

	def getSleep(self, error):
		if !error:
			self._arduino = False
		return 60
