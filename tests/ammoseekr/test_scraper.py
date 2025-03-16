import json
import os
from unittest import mock

import pytest
import requests

from ammoseekr.scraper import Scraper


def read_mock(mock_filename):
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{curr_dir}/mock_data/{mock_filename}", "r") as f:
        return f.read()


@pytest.fixture
def mock_scraper() -> Scraper:
    sess = mock.Mock(requests.Session)
    sess.post.return_value = mock.Mock()
    sess.get.return_value = mock.Mock()
    return Scraper(sess)


def test_list_deals(mock_scraper):
    data = json.loads(read_mock("mock_list.json"))
    mock_scraper.session.post.return_value.json.return_value = data

    results = mock_scraper.list_deals()
    assert len(results) == 2
