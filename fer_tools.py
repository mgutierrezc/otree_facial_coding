import cv2
from fer import FER
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

    test_image_one = plt.imread(f"{img_path}/{img_name}.png")
    emo_detector = FER(mtcnn=True)
        
    # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    return (dominant_emotion, emotion_score)