from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests

__author__ = 'brihopki'
LOGGER = getLogger(__name__)


class TodayHistorySkill(MycroftSkill):

    def __init__(self):
        super(TodayHistorySkill, self).__init__(name="TodayHistorySkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        random_event_intent = IntentBuilder("RandomEventIntent").\
            require("RandomEventKeyword").build()
        self.register_intent(random_event_intent, self.handle_random_event_intent)

    def handle_random_event_intent(self, message):
        url = 'http://history.muffinlabs.com/date'
        r = requests.get(url)
        json_output = r.json()
        output = json_output['data']
        events = output['Events']
        self.speak_dialog('event', data={'event': events[0]['text']})

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return TodayHistorySkill()
