# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
##################################################LIBRARIES###########################################################################
import psycopg2
from psycopg2 import Error
import sqlite3
from sqlite3 import Error
from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
################################################################################################################################



class hr_odoo_duration_timeoff(Action):  #(list all) duration timeoff رصيد الاجازات  #--odoo--#
    def name(self) -> Text:
        return "duration_timeoff"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            connection = psycopg2.connect(
                database="demo",
                user="odoo",
                password="admin",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            query = "select name, duration_display from hr_leave as l left join hr_employee as e on l.id = e.id;"
            cursor.execute(query)
            results = cursor.fetchall()

            message = ""
            for result in results:
                message += f"{result[0]}: {result[1]}\n"
            
            dispatcher.utter_message(message)

        except Error as e:
            dispatcher.utter_message(f"An error occurred while retrieving data from the database: {str(e)}")
        
        return []
    

class hr_odoo_employee_duration_timeoff(Action):  #(only one employee[entity]) duration timeoff رصيد الاجازات  #--odoo--#
    def name(self) -> Text:
        return "employee_duration_timeoff"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:

            #database connection
            connection = psycopg2.connect(
                database="demo",
                user="odoo",
                password="admin",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()   

            # extract entity from message user
            slot_value = tracker.get_slot('employee')

            # all name in company
            query = "select name from hr_employee;"
            cursor.execute(query)
            employees = cursor.fetchall()

            # convert employees into list and store it in employees_list
            employees_list = [list(employee) for employee in employees]
            
            #database query
            query = "select name, duration_display from hr_leave as l left join hr_employee as e on l.id = e.id where e.name = %s"
            cursor.execute(query, (slot_value,))
            results = cursor.fetchall()

            if results:
                message = ""
                for result in results:
                    message += f"{result[0]}: {result[1]}\n"
                dispatcher.utter_message(message)
            else:
                dispatcher.utter_message(f"{slot_value} is not found in the database")




            #check if employee is in the list if not return error
            # if [slot_value] in employees_list:
            #     dispatcher.utter_message(str(results))
            #     pass
            # else: 
            #     dispatcher.utter_message(f"{slot_value} is not found in the database")
            #     pass
            
        except Error as e:
            dispatcher.utter_message(f"An error occurred while retrieving data from the database: {str(e)}")
        
        return []    