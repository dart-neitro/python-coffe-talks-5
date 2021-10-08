# test_core.py

import unittest
from unittest.mock import patch, Mock

from uuid import UUID
from dataclasses import field, dataclass

import core


@dataclass
class NewUser(core.User):
    id: UUID = field(default_factory=Mock(return_value=UUID('11111111-2222-3333-4444-555555555555')))


class MyTest(unittest.TestCase):
    @patch('core.User', NewUser)
    def test_user(self):
        user = core.User(name='Test name')
        assert user.name == 'Test name'
        assert user.id == UUID('11111111-2222-3333-4444-555555555555')