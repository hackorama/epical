import os
import sys
from unittest.mock import patch

if os.path.exists("../epical"):
    sys.path.append("../epical")

if os.path.exists("../grid/lib"):
    sys.path.append("../grid/lib")

from data.cal_data import CalData
import config
from layout import Layout


class TestLayout:

    def build_event_grid(self, mock_get_events, count, length):
        event = "X" * length
        mock_events = {}
        for i in range(count):
            mock_events[str(i)] = event
        mock_get_events.return_value = mock_events
        data = CalData()
        layout = Layout(data, config.SCREEN_W, config.SCREEN_H, config.SCREEN_BORDER)
        grid = layout.build_events_grid()
        return grid.image()

    @patch('data.cal_data.CalData.get_events')
    def test_event_count_layout(self, mock_get_events):
        os.chdir("../epical")  # resolve relative paths to the resources
        width = 787
        height = 372
        max_height = 812
        event_len = 10
        image = self.build_event_grid(mock_get_events, 1, event_len)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 10, event_len)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 11, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
        image = self.build_event_grid(mock_get_events, 25, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
        image = self.build_event_grid(mock_get_events, 26, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
        image = self.build_event_grid(mock_get_events, 1024, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)

    @patch('data.cal_data.CalData.get_events')
    def test_long_event_layout(self, mock_get_events):
        os.chdir("../epical")  # resolve relative paths to the resources
        width = 787
        height = 372
        max_height = 812
        image = self.build_event_grid(mock_get_events, 3, 1)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 32)
        image.save("/tmp/32.png")
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 33)
        image.save("/tmp/33.png")
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 40)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 41)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 64)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 65)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 3, 1024)
        assert (image.width <= width)
        assert (image.height <= height)

    @patch('data.cal_data.CalData.get_events')
    def test_event_count_with_long_event_layout(self, mock_get_events):
        os.chdir("../epical")  # resolve relative paths to the resources
        width = 787
        height = 372
        max_height = 812
        event_len = 64
        image = self.build_event_grid(mock_get_events, 1, event_len)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 10, event_len)
        assert(image.width <= width)
        assert(image.height <= height)
        image = self.build_event_grid(mock_get_events, 11, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
        image = self.build_event_grid(mock_get_events, 25, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
        image = self.build_event_grid(mock_get_events, 26, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
        image = self.build_event_grid(mock_get_events, 1024, event_len)
        assert(image.width <= width)
        assert(image.height <= max_height)
