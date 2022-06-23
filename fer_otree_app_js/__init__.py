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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    base_image = models.LongStringField()
    dominant_emotion = models.StringField()
    emotion_score = models.FloatField()


# PAGES
class Introduction(Page):
    pass


class FacialCapture(Page):
    form_model = "player"
    form_fields = ["base_image"]
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        # TODO: use face recog software
        snapshot_path = "fer_otree_app_js/snapshots"
        snapshot_name = "screen_cap"

        img_fixed_format = player.base_image.replace("data:image/jpeg;base64,", "")
        fer_tools.base64_decoder(img_fixed_format, snapshot_name, snapshot_path)
        

class FacialRecognition(Page):
    pass


page_sequence = [Introduction, FacialCapture, FacialRecognition]
