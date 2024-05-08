import cv2

def extract_first_frame(video_path, output_image_path):
    
    video = cv2.VideoCapture(video_path)

   
    if not video.isOpened():
        print("Error: Could not open video file.")
        return

  
    ret, frame = video.read()

    if not ret:
        print("Error: Could not read the first frame from the video.")
        return

    cv2.imwrite(output_image_path, frame)

    
    video.release()

    print("First frame extracted and saved as", output_image_path)

video_path = "parking_video.mp4"
output_image_path = "parking.jpg"
extract_first_frame(video_path, output_image_path)
