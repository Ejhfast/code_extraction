# OpenCV, area between two curves
Mat src(480,640,CV_8UC3,Scalar(0,0,0));
   ellipse(src,Point(src.cols/2,src.rows/2), Size (src.cols/2,src.rows/2), 0, 0,-180,Scalar(0,0,255), -1,8, 0);
   ellipse(src,Point(src.cols/2,src.rows/2), Size (src.cols/4,src.rows/4), 0, 0,-180,Scalar(0,0,0), -1,8, 0);
