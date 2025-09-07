import cv2 
import numpy as np

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)

marker_id = 80 # Choose an ID from 0 to 99 for DICT_4X4_100 
marker_size = 200 # Size in pixels (e.g., 200x200)

marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8) 
cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_image, 1)

cv2.imwrite(f"aruco_marker_id_{marker_id}.png", marker_image)
cv2.imshow(f"ArUco Marker ID: {marker_id}", marker_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()