import unittest
from unittest.mock import patch


from work_log import Main, Entry
from database import Log


class MenuTests(unittest.TestCase):
    """Test Main Menu"""

    @patch("work_log.Entry.add_log")
    def test_add_Log_option(self, add_mock):
        with patch("builtins.input", side_effect="1"):
            Main().menu_loop()
        add_mock.assert_called_once

    @patch("work_log.View.view_logs")
    def test_view_entries_option(self, view_mock):
        with patch("builtins.input", side_effect="2"):
            Main().menu_loop()
        view_mock.assert_called_once

    @patch("work_log.Main.search_menu_loop")
    def test_search_menu_option(self, search_mock):
        with patch("builtins.input", side_effect="3"):
            Main().menu_loop()
        search_mock.assert_called_once


class SearchMenuTests(unittest.TestCase):
    """Test Search Menu"""

    @patch("work_log.Search.user_search")
    def test_user_search_option(self, user_mock):
        with patch("builtins.input", side_effect="1"):
            Main().search_menu_loop()
        user_mock.assert_called_once

    @patch("work_log.Search.date_search")
    def test_date_search_option(self, date_mock):
        with patch("builtins.input", side_effect="2"):
            Main().search_menu_loop()
        date_mock.assert_called_once

    @patch("work_log.Search.time_search")
    def test_time_search_option(self, time_mock):
        with patch("builtins.input", side_effect="3"):
            Main().search_menu_loop()
        time_mock.assert_called_once

    @patch("work_log.Search.term_search")
    def test_term_search_option(self, term_mock):
        with patch("builtins.input", side_effect="4"):
            Main().search_menu_loop()
        term_mock.assert_called_once


class DatabaseTests(unittest.TestCase):
    """Test Connection to Database"""

    def test_connect_db(self):
        self.assertRaises(Exception, Log().initialize())


class AddLogTests(unittest.TestCase):
    """Test posting data to database"""

    def test_obtain_user_name(self):
        with patch("builtins.input", return_value='Taylor'):
            assert Entry().obtain_user_name() == 'Taylor'

    def test_obtain_task_name(self):
        with patch("builtins.input", return_value='Python'):
            assert Entry().obtain_task_name() == 'Python'

    def test_obtain_task_time(self):
        with patch("builtins.input", return_value=30):
            assert Entry().obtain_task_time() == 30

    def test_obtain_notes(self):
        with patch("builtins.input", return_value='This is a lot of fun!'):
            assert Entry().obtain_notes() == 'This is a lot of fun!'


if __name__ == '__main__':
    unittest.main(exit=False)
