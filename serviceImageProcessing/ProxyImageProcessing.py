from .ImageProcessingService import ImageProcessingService

class ProxyImageProcessing(ImageProcessingService):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def send(self, file_path, image):
        return self._real_subject.send(file_path, image)
        