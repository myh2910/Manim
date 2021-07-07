from pydub import AudioSegment

def flac_to_mp3(dir1, dir2='assets/audio.mp3', frame_rate=44100, channels=2, bitrate='320k'):
	audio = AudioSegment.from_file(dir1, format='flac', frame_rate=frame_rate, channels=channels)
	audio.export(dir2, format='mp3', bitrate=bitrate)

if __name__ == '__main__':
	path1 = '/sda5/Media/Music/한국인이 사랑한 피아노 TOP 100/CD3/12. 서정 소곡집 중 사랑의 시 {Lyric Pieces Op. 43 No. 5 Erotik}.flac'
	flac_to_mp3(path1)
