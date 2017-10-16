import os
import unittest
import dm_man

class DMTestCase(unittest.TestCase):

    def setUp(self):
        dm_man.app.testing = True
        self.app = dm_man.app.test_client()

    def tearDown(self):
        a = a

if __name__ == '__main__':
    unittest.main()