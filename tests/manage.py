# tests/manage.py

# запускает тесты предворительно сформировав необходимые данные

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import unittest, os, shutil
import flamoon

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def test():
    os.makedirs('test_project', exist_ok=True)
    os.system('python3 setup.py install')

    tests = unittest.TestLoader().discover('all_tests',)
    os.system('echo "\n\033[92mTESTS_APP: \033[0m"')
    unittest.TextTestRunner(verbosity=2).run(tests)

    old_chdir = os.path.abspath(os.getcwd())
    new_chdir = old_chdir.rstrip('/test_project') 
    os.chdir(new_chdir)
    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('Flamoon.egg-info')
    shutil.rmtree('test_project')


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
    test()