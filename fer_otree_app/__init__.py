from re import T
from statistics import mode
from otree.api import *
import fer_tools

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
    dominant_emotion = models.StringField()
    emotion_score = models.FloatField()


# PAGES
class Introduction(Page):
    pass


class FacialCapture(Page):
    # TODO: set up livepage for taking photo using webcam
    @staticmethod
    def take_pic(player, data):
        print("data", data)
        player_took_pic = data["player_took_pic"]

        pic_name = "test_pic"
        pic_path = "pic_path"
        if player_took_pic is True:
            fer_tools.picture_taker(pic_name, pic_path)
            player.dominant_emotion, player.emotion_score = fer_tools.facial_emotion_recognizer(pic_name, pic_path)
            

class FacialRecognition(Page):
    pass


page_sequence = [Introduction, FacialCapture, FacialRecognition]
