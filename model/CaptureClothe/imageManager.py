from services.serviceImageProcessing.ProxyImageProcessing import ProxyImageProcessing
from services.serviceImageProcessing.PI4Connector import PI4Connector

def sendPictureToPI(file_path, picture):
    return ProxyImageProcessing(PI4Connector()).send(file_path, picture)
  