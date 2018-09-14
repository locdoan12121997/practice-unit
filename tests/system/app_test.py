from unittest import TestCase
from unittest.mock import patch

import app


class AppTest(TestCase):
    def test_menu_prints_blogs(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input', return_value='q'):
                app.menu()

                mocked_print.assert_called_with('- Test by Test Author (0 posts)')
