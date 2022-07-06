from re import T
from statistics import mode
from tracemalloc import Snapshot
from otree.api import *
import fer_tools

doc = """
Facial Emotion Recognition app in oTree
"""


class C(BaseConstants):
    NAME_IN_URL = 'fer_otree_app_js'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    contact_template = "fer_otree_app_js/Contact.html"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    base_image = models.LongStringField()
    dominant_emotion = models.StringField()
    emotion_score = models.FloatField()


# PAGES
class FacialCapture(Page):
    form_model = "player"
    form_fields = ["base_image"]
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        # snapshot main params
        snapshot_path = "fer_otree_app_js/snapshots"
        snapshot_name = "screen_cap" + "-" + player.participant.code

        # storing snapshot
        img_fixed_format = player.base_image.replace("data:image/jpeg;base64,", "")
        fer_tools.base64_decoder(img_fixed_format, snapshot_name, snapshot_path)

        # performing FER
        player.dominant_emotion, player.emotion_score = fer_tools.facial_emotion_recognizer(snapshot_name, snapshot_path)


class VideoCapture(Page):
    pass


class FacialRecognition(Page):
    def vars_for_template(player):
        return {"b64_picture": player.base_image,
                "dominant_emotion": player.dominant_emotion, 
                "emotion_score": player.emotion_score}


page_sequence = [FacialCapture, FacialRecognition]
