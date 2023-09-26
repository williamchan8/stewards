import cv2
import os

# Specify the path for your video
video_path = 'C:\\Users\\William\\Documents\\stewards\\data\\ham3.mp4'

# Create a directory to save the extracted frames
frames_dir = 'extracted_frames3'
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Open the video
cap = cv2.VideoCapture(video_path)

# Get the total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop over all frames and save each frame as an image
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        print("Failed to retrieve frame")
        break
    
    # Save frame as image
    frame_filename = os.path.join(frames_dir, f"frame_{i}.png")
    cv2.imwrite(frame_filename, frame)

# Release the video capture object
cap.release()
print("Frames extracted and saved to", frames_dir)