# Python Gstreamer record audio from mic and play immediately
autoaudiosrc ! audioconvert ! tee name="source" ! queue ! vorbisenc ! oggmux ! filesink location=file.ogg source. ! queue ! audioconvert ! alsasink
