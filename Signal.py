from scipy.io import wavfile
from numpy import ndarray, arange
from matplotlib import pyplot as plt

class Signal(object):
	def __init__(self):
		self.signal = [] #array to store the signal
		self.stereo = False #boolean that indicates whether the signal is stereo or not

	def read_wav(self, filename):
		tmp = wavfile.read(filename)
		self.rate = tmp[0]
		self.signal = tmp[1]
		if (type(self.signal[0]) == ndarray):
			self.stereo = True
		time_limit = float(len(self.signal))
		time_limit = time_limit / self.rate
		self._time = time_limit

	def write_wav(self, filename):
		if len(self.signal) == 0:
			print "No signal entered yet"
		else:
			wavfile.write(filename, self.rate, self.signal)

	def plot(self):
		if len(self.signal) == 0:
			print "No signal entered yet"
			return

		if not self.stereo:
			frequency_axis = self.signal
		else:
			frequency_axis = []
			for tmp in self.signal:
				nb = (tmp[0] + tmp[1]) / 2
				frequency_axis.append(nb)

		time_limit = self._time
		time_axis = arange(0, time_limit, time_limit / len(frequency_axis))
		plt.plot(time_axis, frequency_axis)
		plt.xlabel("Time")
		plt.ylabel("Frequency")
		plt.show()
