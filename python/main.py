import os

def thumbnail(year, number, quality='k', Scene='Thumbnail'):
	year, number = str(year), str(number)
	os.system(f'python -m manim -q{quality} -o Thumbnail python/t{year}_{number}.py {Scene}')

def video(year, number, quality='k', Scene='Video'):
	year, number = str(year), str(number)
	os.system(f'python -m manim -q{quality} -o IMO_{year}_problema_{number}_yohan_min python/v{year}_{number}.py {Scene}')

if __name__ == '__main__':
	#thumbnail(2015, 4)
	#video(2015, 4)
	#thumbnail(2018, 1)
	#video(2018, 1)
	#thumbnail(2020, 1)
	#video(2020, 1)
	pass
