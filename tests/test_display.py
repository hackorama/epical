import os
import sys
from datetime import datetime
from unittest.mock import patch

if os.path.exists("../epical"):
    sys.path.append("../epical")

import config
from main import run

class TestDisplay:

    @patch('datetime.datetime')
    def test_display(self, mock_datetime):
        test_date = '05/01/23 13:42:42'
        test_date_object = datetime.strptime(test_date, '%m/%d/%y %H:%M:%S')
        mock_datetime.now.return_value = test_date_object
        os.chdir("../epical")  # resolve relative paths to the resources
        try:
            run()
        except Exception as error:
            assert False, f"'Failed with exception: {error}"


