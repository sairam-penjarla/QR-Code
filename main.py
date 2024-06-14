import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Predefined list of access codes
access_codes = ["12345", "67890", "ABCDE"]

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Get frame dimensions
    height, width, _ = frame.shape
    
    # Define the center square (adjust size as needed)
    square_size = 500
    top_left_x = width // 2 - square_size // 2
    top_left_y = height // 2 - square_size // 2
    bottom_right_x = top_left_x + square_size
    bottom_right_y = top_left_y + square_size
    
    # Draw the center square
    cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), 2)
    
    # Decode the QR code in the frame
    decoded_objects = decode(frame)
    
    for obj in decoded_objects:
        # Get the bounding box coordinates
        points = obj.polygon
        if len(points) == 4:
            pts = [(point.x, point.y) for point in points]
            pts = np.array(pts, dtype=np.int32).reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        
        # Get the decoded text
        qr_code_data = obj.data.decode("utf-8")
        
        # Check if the decoded value is in the access_codes list
        if qr_code_data in access_codes:
            text = f"Access Granted: {qr_code_data}"
            color = (0, 255, 0)
        else:
            text = "Access Denied"
            color = (0, 0, 255)
        
        # Display the result
        print(points)
        cv2.putText(frame, text, (points[0][0], points[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 2)
        cv2.putText(frame, text, (points[0][0], points[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    
    # Display the resulting frame
    cv2.imshow('QR Code Scanner', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
