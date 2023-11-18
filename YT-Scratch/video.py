import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the video file
video_capture = cv2.VideoCapture('D:/CodeCode/Afranzio-Sunday/Youtube Automation/YT-Scratch/videos/downloads/video01.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 30.0, (int(video_capture.get(3)), int(video_capture.get(4))))

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Write the modified frame into the output video file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
video_capture.release()
out.release()
cv2.destroyAllWindows()