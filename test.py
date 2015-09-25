import Signal
import os
import shutil
import sys

def test_wav_file(filename):
	wav_file = Signal.Signal()
	wav_file.read_wav("./resources/" + filename)
	wav_file.write_wav("./copy_resources/" + filename)
	wav_file.plot()

try:
	wav_files = os.listdir("./resources/")

	for files in wav_files:
		if not files.endswith(".wav"):
			wav_files.remove(files)

	if len(wav_files) == 0:
		print "Please insert at least one .wav files in the resources folder"
		sys.exit()

	if os.access("copy_resources", os.F_OK):
		shutil.rmtree("copy_resources")
	os.mkdir("copy_resources", 0755)

	for files in wav_files:
		test_wav_file(files)

except Exception as tmp:
	print ""
	print "Problem during the execution:"
	print tmp
