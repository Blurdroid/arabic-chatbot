from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import openai
import requests


class chatgpt_integration(Action):  #chatgpt 
    def name(self) -> Text:
        return "chatgpt_action"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #extract user input
        user_input = tracker.latest_message.get('text')
        
        response = requests.post('https://api.openai.com/v1/chat/completions',
                             headers={'Authorization': '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'},
                             json={'messages': [{'role': 'system', 'content': 'You are a user'}, {'role': 'user', 'content': user_input}]}
                            ).json()
        
        try:
            # Extract the generated response from ChatGPT API
            generated_response = response['choices'][0]['message']['content']
        except KeyError:
            generated_response = "Oops! Something went wrong. Please try again."

        # Send the response back to the user through Rasa
        dispatcher.utter_message(text=generated_response)
        
        return []