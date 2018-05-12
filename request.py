import requests
import numpy as np
import cv2
import math
# from bs4 import BeautifulSoup as bs


EarthRadius = 6378137
MinLatitude = -85.05112878
MaxLatitude = 85.05112878
MinLongitude = -180
MaxLongitude = 180

def Clip(n, minValue, maxValue):
    return min(max(n, minValue), maxValue)

def MapSize(levelOfDetail):
    return 256 << levelOfDetail

def latlon2pix(latitude, longitude, levelOfDetail):
    latitude = Clip(latitude, MinLatitude, MaxLatitude)
    longitude = Clip(longitude, MinLongitude, MaxLongitude)

    x = (longitude + 180) / 360
    sinLatitude = math.sin(latitude * math.pi / 180)
    y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * math.pi)

    mapSize = MapSize(levelOfDetail)
    pixelX = int(Clip(x * mapSize + 0.5, 0, mapSize - 1))
    pixelY = int(Clip(y * mapSize + 0.5, 0, mapSize - 1))
    return pixelX, pixelY


def pixel2tile(pixelX, pixelY):
    tileX = pixelX / 256
    tileY = pixelY / 256
    return tileX, tileY


def quad(tileX, tileY, levelOfDetail):
    key = []
    for i in reversed(range(levelOfDetail)):
        digit = 0
        mask  = 1 << i
        if (tileX & mask !=0):digit += 1 
        if (tileY & mask !=0):digit += 2
        key.append(digit)
    return ''.join(map(str,key))

def display(image, window_name = 'img', delay = 0):
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.imshow(window_name,image)
    cv2.waitKey(delay)
    cv2.destroyAllWindows()


def main():

    '''
    # Extra stuff
    value = {'key':'AoFjYhvMNX80yWOUe58xc2W8Gd_kGVAdPVpJ_t8x3T7lM-sHOHjo0wY2wtBGQX6f','output' : 'xml'}
    r = requests.get('http://dev.virtualearth.net/REST/V1/Imagery/Metadata/Aerial', params=value)
    a= bs(r.content , 'lxml-xml')
    print (a.prettify())
    b = a.find('ImageUrl').contents[0]
    '''
    lat = input ('Enter latitude: ')
    lon = input ('Enter longitude: ')
    levelOfDetail = input('Enter level of detail: ')

    a,b = latlon2pix(lat,lon,levelOfDetail)
    x,y = pixel2tile(a,b)
    qk = quad(x,y,levelOfDetail)
    # http://ecn.t0.tiles.virtualearth.net/tiles
    url  = 'http://ecn.t0.tiles.virtualearth.net/tiles/h' + qk +'.jpeg?g=131'
    r = requests.get(url, stream = True)
    print r.url
    image = np.asarray(bytearray(r.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    display(image)





if __name__ == '__main__':
    main()