from time import sleep
from picamera import PiCamera
from flask import Flask, send_from_directory, request

app = Flask(__name__)

def str_to_int_tuple(str):
    return (int(str.replace("(","").replace(")","").split(",")[0]), int(str.replace("(","").replace(")","").split(",")[1]))

def camera_config(requestArguments):
    """
        This function configures the camera with the necessary parameters
    """
    if requestArguments["framerate"]:
        framerate=float(requestArguments["framerate"])
    else:
        framerate=0.2
    camera = PiCamera(framerate=framerate)

    try: 
        camera.vflip = True
        camera.hflip = True
        camera.shutter_speed = int(requestArguments["shutter_speed"])
        camera.resolution = str_to_int_tuple(requestArguments["resolution"])
        camera.iso = int(requestArguments["iso"])
        sleep(10)
        camera.exposure_mode = requestArguments["exposure_mode"]

        camera.capture('image.jpg')
    finally:
        camera.close()
        
    

@app.route('/')
def capture():
    """
        This function is the root of the served address. This captures an image and puts it up. 
        Default method: GET
        Parameters: 
            resolution=(3280, 2464),
            shutter_speed=10000000,
            iso=800,
            exposure_mode=off,
            framerate=0.1
        sample GET request: /?resolution=(3280,2464)&shutter_speed=10000000&iso=800&exposure_mode=off&framerate=0.1
    """
    camera_config(request.args)

    return send_from_directory('./', "image.jpg")

@app.route('/normal')
def normal():
    """
        Capturing a normal picture with resolution as the parameter:
        GET: resolution=(3280,2464)
    """
    camera = PiCamera()
    try: 
        camera.vflip = True
        camera.hflip = True
        camera.resolution = str_to_int_tuple(request.args["resolution"])
        camera.capture('image.jpg')
    finally:
        camera.close()
    return send_from_directory('./', "image.jpg")

@app.route('/default')
def default():
    """
        Capturing a normal picture with no parameter
    """
    camera = PiCamera()
    try: 
        camera.vflip = True
        camera.hflip = True
        camera.resolution = (1024, 768)
        camera.capture('image.jpg')
    finally:
        camera.close()
    return send_from_directory('./', "image.jpg")

@app.route('/images/<path:path>')
def images(path):
    """
        This function is the root of the served address. This captures an image and puts it up. 
        Default method: GET
        Parameters: 
            resolution=(3280, 2464),
            shutter_speed=10000000,
            iso=800,
            exposure_mode=off,
            framerate=0.1
        sample GET request: /?resolution=(3280,2464)&shutter_speed=10000000&iso=800&exposure_mode=off&framerate=0.1
    """
    return send_from_directory('./images/', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

