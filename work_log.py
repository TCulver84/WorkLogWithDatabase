#!/usr/bin/env python3
"""by doing this you can execute the program with ./filename.py
 after running chmod +x filename.py"""
import datetime
from collections import OrderedDict

from utilities import Utilities
from database import Log


class Main():
    """Contains all methods and variables
    associated with NAVIGATING the menus"""

    def menu_loop(self):
        """show the menu"""
        choice = None
        while choice != 'q':
            Utilities().clear()
            print("Welcome to Work Log 2.0")
            for key, value in menu.items():
                print('{}) {}'.format(key, value.__doc__))
                # __doc__converts variable to function
            print("\nEnter 'q' to quit.")
            choice = input('Menu Selection: ').lower().strip()
            if choice == "1":
                return Entry().add_log()
            elif choice == "2":
                return View().view_logs()
            elif choice == "3":
                return self.search_menu_loop()

    def search_menu_loop(self):
        """Search the Logs"""
        choice = None
        while choice != 'm':
            Utilities().clear()
            print("Enter 'm' to return to main menu.")
            for key, value in search_menu.items():
                print('{}) {}'.format(key, value.__doc__))
                # __doc__converts variable to function
            choice = input('\nSearch Type: ').lower().strip()
            if choice == "1":
                Utilities().clear()
                return Search().user_search()
            elif choice == "2":
                Utilities().clear()
                return Search().date_search()
            elif choice == "3":
                Utilities().clear()
                return Search().time_search()
            elif choice == "4":
                Utilities().clear()
                return Search().term_search()


class Entry():
    """Contains all methods and variables associated
    with ENTERING data into the database"""

    def __init__(self, user_name_data="",
                       task_name_data="",
                       task_time_data=int,
                       notes_data=""):
        self.user_name_data = user_name_data
        self.task_name_data = task_name_data
        self.task_time_data = task_time_data
        self.notes_data = notes_data

    def obtain_user_name(self):
        self.user_name_data = input("Enter your username."
            "Press ENTER when finished\n")
        return self.user_name_data

    def obtain_task_name(self):
        self.task_name_data = input("Enter your task name."
            "Press ENTER when finished\n")
        return self.task_name_data

    def obtain_task_time(self):
        self.task_time_data = input("Enter your task time (in minutes)."
            "Press ENTER when finished\n")
        return self.task_time_data

    def obtain_notes(self):
        self.notes_data = input("Enter your notes."
            "Press ENTER when finished\n")
        return self.notes_data

    def add_log(self):
        """Add a Log"""
        loop = True
        while loop:
            Utilities().clear()
            self.obtain_user_name()
            self.obtain_task_name()
            self.obtain_task_time()
            self.obtain_notes()
            if input('Save Log? [y/n] ').lower() != 'n':
                try:
                    Log().create(user_name=self.user_name_data,
                               task_name=self.task_name_data,
                               task_time=self.task_time_data,
                               notes=self.notes_data)
                    input("Saved Successfully!"
                        "Hit enter to return to main menu")
                    break
                except ValueError:
                    input("ValueError: Time must be INT!"
                        "Press ENTER to try again!")
        return Main().menu_loop()


class View():
    """Contains all methods and variables
    associated with VIEWING data in the database"""

    def __init__(self, log="", logs=""):
        self.log = log
        self.logs = logs

    def view_logs(self, search_query=None, search_type=None):
        """View All Logs"""
        logs = Log.select().order_by(Log.timestamp.desc())
        if search_type == "user_search":
            logs = logs.where(Log.user_name.contains(search_query))
        elif search_type == "date_search":
            logs = logs.where(Log.timestamp.contains(search_query))
        elif search_type == "time_search":
            logs = logs.where(Log.task_time == search_query)
        elif search_type == "term_search":
            logs = logs.where(
                (Log.notes.contains(search_query)) |
                (Log.task_name.contains(search_query)))
        self.paginate_logs(logs)
        return logs

    def paginate_logs(self, logs):
        """Paginate through logs"""
        while True:
            for self.log in logs:
                timestamp = self.log.timestamp.strftime('%A %B %d, %Y %I:%M%p')
                Utilities().clear()
                print(timestamp)
                print('='*len(timestamp))
                # print x '+' values for length of timestamp
                print('User Name:' + self.log.user_name)
                print('Task Name:' + self.log.task_name)
                print('Task Time:' + str(self.log.task_time))
                print('Task Notes:' + self.log.notes)
                print('\n\n'+'='*len(timestamp))
                print('n) next Log')
                print('q) return to main menu')
                print('d) delete_log')
                next_action = input('Action: [Ndq] ').lower().strip()
                if next_action == 'q':
                    return Main().menu_loop()
                elif next_action == 'd':
                    return self.delete_log(self.log)

    def delete_log(self, log):
        """Delete an Log"""
        if input("Are you sure? [yN] ").lower() == 'y':
            self.log.delete_instance()
            input("Log deleted! Press ENTER to continue")
            return Main().menu_loop()


class Search():
    """contains all methods and variables
    associated with SEARCHING the database"""

    def user_search(self):
        """Search Logs by User Name"""
        logs = Log.select(Log.user_name).order_by(Log.user_name.asc())
        print("These Are the Availible Names:")
        values = []
        for log in logs:
            print(log.user_name)
            values.append(log.user_name.lower())
        user_name = input('\nFind by User Name: ').lower()
        if user_name not in values:
            input("\nSorry! No values were returned for that search!",
                  ", Press ENTER to return to main menu")
            values = []
            return Main().menu_loop()
        else:
            return View().view_logs(user_name, "user_search")

    def date_search(self):
        """Search Logs by Date"""
        logs = Log.select(Log.timestamp).order_by(Log.timestamp.desc())
        print("These Are the Availible Dates:")
        values = []
        for log in logs:
            value = log.timestamp.strftime('%m/%d/%Y')
            print(value)
            values.append(value)
        timestamp = input('\nFind by Time Stamp (Copy From Above): ')
        if timestamp not in values:
            input("\nSorry! No values were returned for that search!,"
                  " Press ENTER to return to main menu")
            values = []
            return Main().menu_loop()
        else:
            reformatted_timestamp = datetime.datetime.strptime(
                timestamp, '%m/%d/%Y').strftime('%Y-%m-%d')
            return View().view_logs(reformatted_timestamp, "date_search")

    def time_search(self):
        """Search Logs by Task Time"""
        logs = Log.select(Log.task_time).order_by(Log.task_time.asc())
        print("These Are the Task Times:")
        values = []
        for log in logs:
            print(log.task_time)
            values.append(log.task_time)
        task_time = input('\nFind by Task Time: ')
        task_time_int = int(task_time)
        if task_time_int not in values:
            input("\nSorry! No values were returned for that search!,"
                  " Press ENTER to return to main menu")
            values = []
            return Main().menu_loop()
        else:
            return View().view_logs(task_time_int, "time_search")

    def term_search(self):
        """Search Logs by Task Name and Notes"""
        search_term = input('Find by value in Task Name or Notes: ')
        return View().view_logs(search_term, "term_search")


menu = OrderedDict([
    ('1', Entry().add_log),
    ('2', View().view_logs),
    ('3', Main().search_menu_loop),
    ])


search_menu = OrderedDict([
    ('1', Search().user_search),
    ('2', Search().date_search),
    ('3', Search().time_search),
    ('4', Search().term_search),
    ])


if __name__ == '__main__':
    Log().initialize()
    Main().menu_loop()
