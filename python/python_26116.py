# cliping a webm file using moviepy and ffmpeg parameters
myclip.write_videofile("test_1.webm", bitrate="50k") # low quality.
myclip.write_videofile("test_2.webm", bitrate="50000k") # high quality.
