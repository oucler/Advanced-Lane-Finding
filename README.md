# Advance Lane Finding

Goal of this project is to detect lanes on highway and output an annotated video which indicates regions of the lane with additional information. In order to detect lanes properly there are few steps are followed as listed below. 


**Project Videos:**


[Project Video](https://www.youtube.com/watch?v=9HRHobSYhRE)

[Challenge Video](https://www.youtube.com/watch?v=mK_2OEAul3A)

-  Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
-  Apply a distortion correction to raw images.
-  Use color transforms, gradients, etc., to create a thresholded binary image.
-  Apply a perspective transform to rectify binary image ("birds-eye view").
-  Detect lane pixels and fit to find the lane boundary.
-  Determine the curvature of the lane and vehicle position with respect to center.
-  Warp the detected lane boundaries back onto the original image.
-  Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.


video_generation.py is the main code that makes functions calls.lanehelper.py, LaneDetector.py, Line.py, and ImageUtils.py are the helper functions.


#### 1. Camera Calibration:


20 sample chessboard images were used for calibrating the camera. Initial step is to populate imagepoints and objectpoints then find and draw identified corners. As final two steps: undistort the image and warped the image. As an example one of the sample images are shown below from the original to warped image.  

**Warped Chessboard Flow:**

![[Warped Image]](camera_cal_out/WarpedBoard.PNG)



####2. Generating Binary Image and Finding Lane Boundary:


Starting from original up to warped image steps are the same but we need additional processes in order to generate a binary image with leaving only desired lines. Lines are not linear and we need to fit onto a two degree polynomial equation. After solving the curvature of birds eye view the   

**Warped Image Flow:**

![[Warped Image]](test_images_out/WarpedImage.PNG)

**Binary Image:**

Gradient and sobel threshold applied to detect the lanes for the project_video but for the challenge video combination of gradient direction/gradient and sobel threshold used along with image processing techniques to detect under different light conditions. 


![[Warped Image]](test_images_out/BinaryImage.PNG)

**Sliding Windows:**

From the binary image histogram applied to find a peak which is a good indicator for x-position of base lane lines. It is used as a starting point for where to search for the lines. From that point, using a sliding window, placed around the line centers, to find and follow the lines up to the top of the frame.


![[Warped Image]](test_images_out/SlidingWindows.PNG)

**Drawn Lines:**

The green shaded area shows where we searched for the lines this time. So, once you know where the lines are in one frame of video, you can do a highly targeted search for them in the next frame. This is equivalent to using a customized region of interest for each frame of video, and should help you track the lanes through sharp curves and tricky conditions. 

![[Drawn Image]](test_images_out/DrawnLines.PNG)


####3. Visual of Lane Boundaries and Status Information:

In above, which pixels belong to left and right lane lines are determined then those pixel positions are fitted with a polynomial equation. To calculate the curve equations below for x/y and x is ignored because it is almost vertical.


f(y)=Ay**​2+By+C


![[Boundary Image]](test_images_out/Curvature.PNG)


####4. Discussions:

For roads conditions with high light contrast such as bright or shadow it is challenging to detect lane lines. Thus, it requires more computer vision techniques to identify lanes correctly. Also, mountain roads are more challenging to detect because curvature changes more frequently.Boundary region needs to be constrained to a much smaller area. 


