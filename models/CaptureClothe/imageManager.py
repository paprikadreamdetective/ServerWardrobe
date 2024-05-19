from serviceImageProcessing.ProxyImageProcessing import ProxyImageProcessing
from serviceImageProcessing.PI4Connector import PI4Connector

def sendImage(image):
    ProxyImageProcessing(PI4Connector()).send(image)