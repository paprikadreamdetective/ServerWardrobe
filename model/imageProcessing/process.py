from ultralytics import YOLO
from rembg import remove


def remove_backgroud_image(input_image, output_image):
    if input_image.endswith(('.png', 'jpg', 'jpeg')): 
        with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
            backgroud_output = remove(inp.read())
            outp.write(backgroud_output)
    else:
        print("The file is not valid")


def do_detection(image) -> str:
    """
    Detections :
        - dress
        - hat
        - longsleeve
        - outwear
        - pants
        - shirt
        - shoes
        - shorts
        - skirt
        - t-shirt
    """
    model = YOLO('./model/imageProcessing/clothes_classification.pt')
    results = model(image, verbose=False)
    for r in results:
        probs = r.probs
        names = r.names
        clothe = probs.top1

    clothing_detected = names[clothe]
    return clothing_detected


def process_image(in_image, out_image):
    remove_backgroud_image(in_image, out_image)
    clothe = do_detection(out_image)
    return clothe
