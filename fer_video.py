from fer import Video
from fer import FER

video_filename = "one_min.mp4"
video = Video(video_filename)

# Analyze video, displaying the output
detector = FER()

# Video class splits video into frames
raw_data = video.analyze(detector, display=True)

df = video.to_pandas(raw_data)
print(df)
