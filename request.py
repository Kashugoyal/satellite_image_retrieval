
import requests
import numpy as np
import cv2




r = requests.get('http://h0.ortho.tiles.virtualearth.net/tiles/h023131022213211200.jpeg?g=131')
cv2.namedWindow("window_name",cv2.WINDOW_NORMAL)
image = np.asarray(bytearray(r.content), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow("window_name",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

