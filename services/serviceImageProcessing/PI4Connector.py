import requests
from .ImageProcessingService import ImageProcessingService 

class PI4Connector(ImageProcessingService):
    def __init__(self):
        self._RASPBERRY_PI_SERVER_URL = 'http://192.168.100.152:8008/receive_image'

    def send(self, file_path, picture):
        with open(file_path, 'rb') as image_file:
            files = {'file': (picture.filename, image_file, picture.content_type)}
            response = requests.Session().post(self._RASPBERRY_PI_SERVER_URL, files=files)

        if response.status_code == 200:
            return True
            #return jsonify({"message": "Image received and forwarded successfully!", "file_path": file_path})
        else:
            return False
            #return jsonify({"message": "Image received but failed to forward", "error": response.text}), 500