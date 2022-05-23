# uwuPose
## (based on Mediapipe-VR-Fullbody-Tracking)

### Problem Definition: 
- Perform Fullbody Tracking in VR
  - Minimally: tracking data for hips, 2 legs
- nothing attached to user
- do not want to modify hardware - it must be off-the-shelf-available.

### This Solution: 
- Input: 2D RGB images from at least 2 webcams
- Using Mediapipe 2D pose estimation, obtain 2D estimation of each keypoint of the person
  - (for each point, give X,Y coordinates in the 2D image plane).
- then, use aniposelib to perform triangulation into 3D 
  - (N x 2D -> 1 x 3D, where N is camera_count)
- Then, perform linear transformation to convert these 3D points into the VR reference frame.
- Finally, send the 3D points to SteamVR via the driver.

### Limitations of solution:
- you need at least 2 cameras to run the algo (triangulation requires >=2 points, one from each camera).
- more cameras at strategic angles will improve self-occlusion issues
- If the hmd's reference frame drifts/is re-initalised at runtime (I would suppose, especially for the inside-out localisation like quest), then our tracker points will require a new transformation to the VR reference frame.

### Pros of vision based
- no need for attaching anything to yourself
- similar principle to quest 2's hand tracking 2.0 (owo, what's this?)
- might be cheaper than buying trackers
- It can improve as the inference model improves

### Cons of vision based
- Complex.
- Requires webcams and mounting height
- inference is run on CPU
- calibration using Aruco Board is required. Non-trivial
- occlusions and self-occlusions. 
- Compared to IMU tech, We lack dead-reckoning to compensate against temporary occlusion.

