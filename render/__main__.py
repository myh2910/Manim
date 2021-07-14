import os
from datetime import datetime
from pydub import AudioSegment

def thumbnail(year, number, quality='k', scene='Thumbnail'):
	year, number = str(year), str(number)
	os.system(f'python -m manim -q{quality} -o Thumbnail render/t{year}_{number}.py {scene}')

def video(year, number, quality='k', scene='Video'):
	year, number = str(year), str(number)
	os.system(f'python -m manim -q{quality} -o IMO_{year}_problema_{number}_yohan_min render/v{year}_{number}.py {scene}')

def format_convert(from_dir, to_dir=None, from_format='flac', to_format='mp3'):
	if to_dir == None:
		to_dir = 'assets/{}.mp3'.format(datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-4])
	audio = AudioSegment.from_file(from_dir, format=from_format)
	audio.export(to_dir, format=to_format)

for args in [(2015, 4), (2018, 1), (2020, 1)]:
	thumbnail(*args)
	video(*args)
