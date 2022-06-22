from re import T
from otree.api import *
import cv2


doc = """
Facial Emotion Recognition app in oTree
"""


class C(BaseConstants):
    NAME_IN_URL = 'fer_otree_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Introduction(Page):
    pass


class FacialCapture(Page):
    # TODO: set up livepage for taking photo using webcam
    @staticmethod
    def take_pic(player, data):
        player_took_pic = data["player_took_pic"]
        if player_took_pic is True:

            cap = cv2.VideoCapture(0) # initializing webcam

            # Check if the webcam is opened correctly
            if not cap.isOpened():
                raise IOError("Cannot open webcam")
            
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

            




class FacialRecognition(Page):
    pass


page_sequence = [Introduction, FacialCapture, FacialRecognition]
