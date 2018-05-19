# Satelite Image Retrieval
### Retieve highest resolution aerial image of a given Latitude-Longitude bounding box using Bing Maps API
---

### Dependencies

1. [Numpy](http://www.numpy.org/)
2. [OpenCv](https://opencv.org/)
3. [Python Requests](http://docs.python-requests.org/en/master/user/install/)


### Execution

* **Method 1**
   Convert the python script into executable and run it directly from the command line.
   ```
   $ chmod +x request.py
   $ ./request.py
   ```
* __Method 2__
   Run the file using `Python` 
   ```
   $ python request.py 
    ```

### Approach
* The program expects a latitude-longitude bounding box for which the image is to be retrieved. The box is defined using two diagonally oppositte points.
* Latitude and longitude values are converted to pixel values based on the highest level of detail (starting with `23`) and this is followed by getting tile numbers for respective pixels. 
* Once we get the tiles for the corners, a loop iterates through all the intermediate tiles, generating quadkey for each and getting corresponding images. 
* If the image is `blank`, the loop breaks and restarts with a level of detail one lower than the previous one. 
* Once all the images are retrieved, they are stiched together to generate one single image.
* The stitched image is then cropped to the bounding box using the pixel values obtained in the second step. The final image is displayed and is also saved in the current directory as `output.png`

   > `Blank` image refers  to the empty image returned by the request response. A simple element by element comparison is used to determine if the obtained image is blank or not.


### Output 
The output of the program is the aerial image of the given bounding box in the highest possible resolution.

### Reflections
* For large bounding boxes, the number of images is very large and the program completion time is very large. Solutions such as multi process threading may be useful.

### Sources
* [Bing Maps Tile System](https://msdn.microsoft.com/en-us/library/bb259689.aspx)
