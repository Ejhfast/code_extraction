# command line closes too fast inside python using ffmpeg
t = 'ffmpeg -r'+str(ctx.field("FrameRate").value)+'-f image2 -pix_fmt yuv420p -s 1920x1080 -i'+path+'%0d.png -vcodec libx264 -crf 15'+path+'.mp4'
log_path = r'C:\log.txt'
os.system(t + ' &gt;&gt; ' + log_path + ' 2&gt;&amp;1')
