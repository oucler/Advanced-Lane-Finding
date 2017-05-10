import os,glob
import argparse
import numpy as np
from moviepy.video.io.VideoFileClip import VideoFileClip
from LaneDetector import LaneDetector

VIDEO_INDEX = 0

#/// \ generateVideo class inherits from LaneDetector class
#/// \ args passed as a variables
class generateVideo(LaneDetector):
    def __init__(self,args):
        LaneDetector.__init__(self,args)
        self.video_dir = args.video_dir
        self.video_list = []
    #/// \ Parse images for camera calibration
    def parse_dir(self):
        #TODO: Change project_video.mp4 to more generic
        if (len(self.video_list) == 0):
            for video in glob.glob(os.path.join(self.video_dir,'project_video.mp4')):
                self.video_list.append(video)
            return self.video_list
        else:
            return self.video_list
    #/// \ Calibrate camera and plots images from original to warped images
    #/// \ images are saved to camera_cal_out folder and test_images_out
    def calibration(self):
        self.run_calibration(index=0,row=1,col=3,visual=True)
    #/// \ Binary Image generated from original image
    #/// \ plotting images
    def generate_binary_image(self):
        images = {}      
        src = np.float32(
                [[(self.img_size[0] / 2) - 55, self.img_size[1] / 2 + 100],
                [((self.img_size[0] / 6) - 10), self.img_size[1]],
                [(self.img_size[0] * 5 / 6) + 60, self.img_size[1]],
                [(self.img_size[0] / 2 + 55), self.img_size[1] / 2 + 100]])
        dst = np.float32(
                [[(self.img_size[0] / 4), 0],
                [(self.img_size[0] / 4), self.img_size[1]],
                [(self.img_size[0] * 3 / 4), self.img_size[1]],
                [(self.img_size[0] * 3 / 4), 0]])
        
        img = self.read_image(list(self.dict_raw_image.values())[4])
        orig_img = np.copy(img)
        
        img = self.bgr2rgb(img)
        images["Original_Image"] = img
            
        undistorted_img = self.undistort(img)
        images["Undistorted_image"] = undistorted_img
        
        warped_image = self.transform(undistorted_img,src,dst)
        images["Warped_Image"] = warped_image
        
        self.visualize(images,row=1,col=3)
        self.binary(warped_image,visual=True)
        self.save_img(images,self.test_out_dir)
        
        self.sliding_windows(warped_image)        
        self.draw(warped_image)  
        
        self.draw_lines(orig_img,img,src,dst)
    #/// \ Processing video frame by frame   
    def generate(self):
       self.parse_dir()

       clip1 = VideoFileClip(self.video_list[VIDEO_INDEX])
       project_clip = clip1.fl_image(self.process_frame)
       
       project_output = self.video_list[VIDEO_INDEX][:-4] + '_out.mp4'
       project_clip.write_videofile(project_output, audio=False)

        

def main():             
    parser = argparse.ArgumentParser(description="Advance Lane Finding Project 3")
    parser.add_argument('-d', help='calibration image directory', dest='cal_dir',type=str,default='camera_cal')
    parser.add_argument('-cn', help='chess board column number', dest='col_num', type=int, default=9)    
    parser.add_argument('-rn', help='chess board row number', dest='row_num', type=int, default=6)  
    parser.add_argument('-rw', help='raw image directory', dest='raw_dir', type=str, default='test_images')
    parser.add_argument('-o',help='adding +/- offset',dest='offset',type=int,default=65)
    parser.add_argument('-thmin', help='min threshold for color space',dest='threshold_min',type=int,default=150)
    parser.add_argument('-thmax',help='max threshold for color space', dest='threshold_max',type=int,default=200)
    parser.add_argument('-vd', help='vidoe directory', dest='video_dir', type=str, default='videos')
    parser.add_argument('-f',help='number of frames',dest='n_frames',type=int,default=7) 
    parser.add_argument('-offset',help='transform offset',dest='transform_offset',type=int,default=250) 
    parser.add_argument('-codir',help='calibration output directory',dest='cal_o_dir',type=str,default='camera_cal_out') 
    parser.add_argument('-todir',help='test images output directory',dest='test_o_dir',type=str,default='test_images_out')     
    parser.add_argument('-ls',help='line segments',dest='line_segments',type=int,default=10) 
    args = parser.parse_args()
    #/// \ Instantiating generateVideo
    #/// \ call calibration()
    #/// \ call generate_binary_image()
    #/// \ call generate video
    gv = generateVideo(args)
    gv.calibration()
    gv.generate_binary_image()
    gv.generate()

if __name__ == '__main__':
    main()
