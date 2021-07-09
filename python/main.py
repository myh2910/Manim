import os
import time
from pydub import AudioSegment

def thumbnail(year, number, quality='k', Scene='Thumbnail'):
	year, number = str(year), str(number)
	os.system(f'python -m manim -q{quality} -o Thumbnail python/t{year}_{number}.py {Scene}')

def video(year, number, quality='k', Scene='Video'):
	year, number = str(year), str(number)
	os.system(f'python -m manim -q{quality} -o IMO_{year}_problema_{number}_yohan_min python/v{year}_{number}.py {Scene}')

def flac_to_mp3(from_dir, to_dir=None, frame_rate=44100, channels=2, bitrate='320k'):
	if to_dir == None:
		to_dir = time.strftime('assets/%Y%m%d_%H%M%S_%2N.mp3', time.localtime())
	audio = AudioSegment.from_file(from_dir, format='flac', frame_rate=frame_rate, channels=channels)
	audio.export(to_dir, format='mp3', bitrate=bitrate)

if __name__ == '__main__':
	for args in [(2015, 4), (2018, 1), (2020, 1)]:
		thumbnail(*args)
		video(*args)
