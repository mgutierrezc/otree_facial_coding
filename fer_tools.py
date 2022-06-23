import cv2, base64
from fer import FER
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt 


def picture_taker(img_name, img_path):
    """
    Opens webcam and captures facial pic

    Input: Image name and path (str)
    Output: None
    """
    
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 32:
            # SPACE pressed
            img_name = f"{img_path}/{img_name}.png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break

    cam.release()

    cv2.destroyAllWindows()


def facial_emotion_recognizer(img_name, img_path):
    """
    Recognizes emotions from a stored picture

    Input: Image name and path (str)
    Output: Dominant emotion (str) and Score (Float)
    """

    test_image_one = plt.imread(f"{img_path}/{img_name}.jpeg")
    emo_detector = FER(mtcnn=True)
        
    # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    return (dominant_emotion, emotion_score)


def base64_decoder(b64_string, img_name, img_path):
    """
    Converts a base 64 image to png format

    Input: Base 64 image (string)
    Output: None
    """

    # converting b64 str to to img object
    byte_img = bytes(b64_string, "utf-8")
    decoded_bytes = base64.decodebytes(byte_img)
    img = Image.open(BytesIO(decoded_bytes)) 

    # storing img on designated path
    filename = f"{img_path}/{img_name}.jpeg"
    img.save(filename)
