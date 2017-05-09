# Advance Lane Finding

Goal of this project is to detect lanes on highway and output an annotated video which indicates regions of the lane with additional information. In order to detect lanes properly there are few steps are followed as listed below. 

**Project Video:**
![[Project Video]](https://www.youtube.com/watch?v=9HRHobSYhRE)


  <iframe width="560" height="315" src="https://www.youtube.com/watch?v=9HRHobSYhRE" frameborder="0" allowfullscreen></iframe>

-  Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
-  Apply a distortion correction to raw images.
-  Use color transforms, gradients, etc., to create a thresholded binary image.
-  Apply a perspective transform to rectify binary image ("birds-eye view").
-  Detect lane pixels and fit to find the lane boundary.
-  Determine the curvature of the lane and vehicle position with respect to center.
-  Warp the detected lane boundaries back onto the original image.
-  Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.


video_generation.py is the main code that makes functions calls.lanehelper.py, LaneDetector.py, and Line.py are the helper functions.

#### 1. Camera Calibration:

20 sample chessboard images were used for calibrating the camera. Initial step is to populate imagepoints and objectpoints then find and draw identified corners. As final two steps: undistort the image and warped the image. As an example one of the sample images are shown below from the original to warped image.  

**Warped Chessboard Flow:**
![[Warped Image]](camera_cal_out/WarpedBoard.PNG)



#### 2. Generating Binary Image and Finding Lane Boundary:

Starting from original up to warped image steps are the same but we need additional processes in order to generate a binary image with leaving only desired lines. Lines are not linear and we need to fit onto a two degree polynomial equation. After solving the curvature of birds eye view the   

**Warped Image Flow:**
![[Warped Image]](test_images_out/WarpedImage.PNG)

**Sliding Windows:**

![[Warped Image]](test_images_out/SlidingWindows.PNG)

**Drawn Lines:**

![[Warped Image]](test_images_out/DrawnLines.PNG)





