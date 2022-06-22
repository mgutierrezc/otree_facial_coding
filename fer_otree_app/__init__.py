from otree.api import *


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


class FacialCapture(WaitPage):
    pass


class FacialRecognition(Page):
    pass


page_sequence = [Introduction, FacialCapture, FacialRecognition]
