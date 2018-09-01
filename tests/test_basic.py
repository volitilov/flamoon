
#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from unittest import TestCase
from ..flamoon.cli import main

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class HelloworldTestCase(TestCase):
    def test_helloworld(self):
        self.assertEqual(main(), 'Hello world')
