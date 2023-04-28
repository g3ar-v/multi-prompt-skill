import random

from adapt.intent import IntentBuilder
from core import Message, MycroftSkill, intent_handler


class MultiPromptSkill(MycroftSkill):

    def __init__(self):
        super(MultiPromptSkill, self).__init__(name="MultiPromptSkill")

    def initialize(self):
        # self.add_event('mycroft.skill.handler.complete', self.handler_skill_complete)
        self.add_event('question:action', self.handler_action)

    def handler_skill_complete(self, message):
        # response = self.get_response('prompt.user')
        self.bus.emit(Message('mycroft.mic.listen'))

        # if self.voc_match(response, 'thanks'):
        # self.speak_dialog("thankyou")

    @intent_handler(IntentBuilder("").require("thanks"))
    def handle_complement(self, event):
        self.speak_dialog("thankyou")

    def handler_action(self, message):
        
        random_num = random.randint(0,1)

        if random_num == 1:
            response = self.get_response('prompt.user')

            if self.voc_match(response, 'thanks'):
                self.speak_dialog("thankyou")

    # def converse(self, message):
    #     if self.voc_match(message.data['utterances'][0], 'thankyou'):
    #         self.speak_dialog("thankyou")


def create_skill():
    return MultiPromptSkill()
