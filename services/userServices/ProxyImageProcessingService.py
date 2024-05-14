from .ImageProcessingService import ImageProcessingService

class ProxyImageProcessing(ImageProcessingService):
    """
    Clase Proxy de ImageProcessingService.
    """

    def __init__(self, real_service):
        self._real_service = real_service

    def process_image(self, image):
        
        # se llama al servicio de clima
        return self._real_service.process_image(image)
