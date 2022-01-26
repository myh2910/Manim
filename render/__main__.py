import os
import time
from datetime import datetime
from pydub import AudioSegment

def video(year, number, quality="k", extra=None, scene="Video"):
	year, number = str(year), str(number)
	title = f"IMO_{year}_problema_{number}_yohan_min"
	command = "python -m manim"
	if extra:
		command += f" {extra}"
	command += f" -q{quality} -o {title} render/v{year}_{number}.py {scene}"
	start = time.time()
	os.system(command)
	end = time.time()
	print(f"{end - start} seconds elapsed.")

def format_convert(from_dir, to_dir=None, from_format="flac", to_format="mp3"):
	if to_dir == None:
		to_dir = "assets/{}.mp3".format(datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-4])
	audio = AudioSegment.from_file(from_dir, format=from_format)
	audio.export(to_dir, format=to_format)
