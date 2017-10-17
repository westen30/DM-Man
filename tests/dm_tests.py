"""DM Manager Test Runner"""
import os
import unittest
import tempfile
from dm_man.dm import create_app

class DMTestCase(unittest.TestCase):

    def setUp(self):
        
        self.db_fd, temp_db_location = tempfile.mkstemp()
        config = {
            'DATABASE': temp_db_location,
            'TESTING': True,
            'DB_FD': self.db_fd
        }
        app = create_app(config)

        with app.app_context():
            #init_db()
            yield app

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()