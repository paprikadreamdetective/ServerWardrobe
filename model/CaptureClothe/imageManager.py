from serviceImageProcessing.ProxyImageProcessing import ProxyImageProcessing
from serviceImageProcessing.PI4Connector import PI4Connector

def sendPictureToPI(file_path, picture):
    return ProxyImageProcessing(PI4Connector()).send(file_path, picture)
    '''
    if ProxyImageProcessing(PI4Connector()).send(file_path, picture):
        return True
    else:
        return False
    '''
    
#def sendImage(image):
#    ProxyImageProcessing(PI4Connector()).send(image)