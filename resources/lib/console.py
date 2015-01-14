import signal, sys;

__should_exit__ = False

def handler(signum, frame):
	global __should_exit__
	__should_exit__ = True

class Model(object):
	def __init__(self):
		signal.signal(signal.SIGINT, handler)

	def notification(self, line1):
		print line1

	def abortRequested(self):
		return __should_exit__

	def read(self):
		pass

	def hasChanged(self):
		return False

	def getServer(self):
		return 'home.vicenteobregon.com'

	def getCheck(self):
		return 1

	def getCount(self):
		return 3

	def getNotify(self):
		return True

	def getSong(self):
		return '\a'

	def play(self, song):
		print song

	def getSleep(self, error):
		if error:
			return 1
		else:
			return 60
