from flask import Flask, request, Response
import time
import base64
import cv2
import base64
from PIL import Image
import numpy as np

PATH_TO_TEST_IMAGES_DIR = './images'

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./static/getImage.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    blob = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    print("images saved!!!!!!!")

    # convert blob into Image
    image_object = Image.open(blob)
    print("PROPERTIES=",image_object)
    image_object.show()
    # Converting Image into Numpy array for prepocessing
    image_np = load_image_into_numpy_array(image_object)
    print(type(image_np),image_np.shape)

    # blob.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, "realTime.jpeg"))
    
    # Sending respone to webpage as f
    return Response("%s saved" % f)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
