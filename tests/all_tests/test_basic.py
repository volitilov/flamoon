
#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import subprocess
import os, sys
from unittest import TestCase
from flamoon.app import app

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class FlamoonStart_test(TestCase):
    def test_initApp(self):
        self.assertTrue(os.path.exists('test_project') == True)
        self.assertTrue(os.path.exists('build') == True)
        self.assertTrue(os.path.exists('dist') == True)

        os.chdir('test_project')
        self.assertTrue(os.getcwd() == os.path.abspath(''))

        res = subprocess.getstatusoutput('flamoon init')
        self.assertTrue(res[0] == 0)


    def test_runApp(self):
        try:
            from threading import Thread
            import requests, time
            import pyautogui as pg

            def test():
                os.system('python3 manage.py run')
                
            th = Thread(target=test)
            th.daemon = True
            th.start()

            time.sleep(4)
            resp = requests.get('http://127.0.0.1:5000/')
            self.assertTrue(resp.status_code == 200)
            pg.hotkey('ctrl', 'c')
            
        except SystemExit: pass
