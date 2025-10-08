import subprocess

def convert(opus_in, mp3_out):
    subprocess.run(['ffmpeg', '-i', opus_in, mp3_out], check=True)

# convert('audio_raw/laksh/in/WhatsApp Audio 2025-10-08 at 23.08.03.opus', 'audio_raw/laksh/out/first.mp3')

convert('audio_raw/laksh/in/WhatsApp Audio 2025-10-08 at 23.08.30.opus', 'audio_raw/laksh/out/two.mp3')

convert('audio_raw/laksh/in/WhatsApp Audio 2025-10-08 at 23.08.49.opus', 'audio_raw/laksh/out/three.mp3')