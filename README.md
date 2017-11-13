Synopsis
The CSV timesheets were a huge success but some more features are needed, including the ability for other developers to use the data without worrying about file locking or availability. The managers have also asked for a way to view time entries for each employee. Seems like a database would be a better solution than a CSV file!

Create a command line application that will allow employees to enter their name, time worked, task worked on, and general notes about the task into a database. There should be a way to add a new entry, list all entries for a particular employee, and list all entries that match a date or search term. Print a report of this information to the screen, including the date, title of task, time spent, employee, and general notes.


Code Example

The codebase is broken into 4 files:

work_log.py -> all classes and functions that contain the business logic of the work log application
tests.py -> all automated regression tests for the work log application
utilities.py -> all classes and functions that do not contain business logic (i.e. clear)
database.py -> all classes and functions that instantiate the local SQLLite database


Motivation

The motivation for this project was to be able to log data to a database and then be able to search the contents via multiple data types and search conditions using object oriented programming and date time data validation.


Installation

To install the project download all files to a location of your choosing on your computer, log into the terminal (on a MAC) and instantiate the program from the directory where you stored the files as follows:

python3 -i work_log.py


Tests

To test the application - please run the following commands and navigate to 0.0.0.0:8000 in your browser to navigate the coverage HTML report

coverage run tests.py
coverage report -m
coverage html
python3 -m http.server 8000


Contributors

This project was inspired by the teachers at teamtreehouse.com and was developed by Taylor. This code as been tested by flake8 PEP8 standards and passes the programmatic testing of all files associated with this application.


License

Opensource for your enjoyment!