# member of audio group cant access /dev/dsp to play sound
python -c "freq=220;sec=2;from math import sin,pi;rate=8000;w=[chr(127+int(127*sin(i*2*pi*freq/rate))) for i in xrange(rate)]*sec;s=''.join(w);print s"  &gt; tmp_sound
 pacat tmp_sound    &gt;padsp
