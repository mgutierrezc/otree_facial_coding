from re import T
from statistics import mode
from tracemalloc import Snapshot
from otree.api import *
import fer_tools

doc = """
Facial Emotion Recognition app in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'fer_otree_app_js'
    players_per_group = None
    num_rounds = 1
    contact_template = "fer_otree_app_js/Contact.html"
    minutes = 2
    batches=[]
    for x in range(1, minutes + 1):
        batches.append('batch_' + str(x) )




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    for subject in Constants.batches:
        locals()[subject] = models.LongStringField()
    del subject
    dominant_emotion = models.StringField()
    emotion_score = models.FloatField()


# PAGES
class FacialCapture(Page):
    form_model = "player"
    lista = Constants.batches
    form_fields = lista

    def vars_for_template(self):
        return dict(label=self.participant.label, minutes=Constants.minutes)
    
    # @staticmethod
    # def before_next_page(player, timeout_happened):
    #     # snapshot main params
    #     snapshot_path = "fer_otree_app_js/snapshots"
    #     snapshot_name = "screen_cap" + "-" + player.participant.code

    #     # storing snapshot
    #     img_fixed_format = player.base_image.replace("data:image/jpeg;base64,", "")
    #     fer_tools.base64_decoder(img_fixed_format, snapshot_name, snapshot_path)

    #     # performing FER
    #     player.dominant_emotion, player.emotion_score = fer_tools.facial_emotion_recognizer(snapshot_name, snapshot_path)


class VideoCapture(Page):
    pass


class FacialRecognition(Page):
    def vars_for_template(player):
        return {"b64_picture": player.base_image,
                "dominant_emotion": player.dominant_emotion, 
                "emotion_score": player.emotion_score}


page_sequence = [FacialCapture, FacialRecognition]
