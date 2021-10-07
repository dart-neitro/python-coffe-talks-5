# test_core.py

import unittest
from unittest.mock import patch, Mock

from uuid import UUID

from core import User


class MyTest(unittest.TestCase):
    @patch('core.uuid4', Mock(return_value=UUID('11111111-2222-3333-4444-555555555555')))
    def test_user(self):
        user = User(name='Test name')
        assert user.name == 'Test name'
        assert user.id == UUID('11111111-2222-3333-4444-555555555555')  # fail here
