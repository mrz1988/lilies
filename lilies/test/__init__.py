import unittest

def test_all(verbosity=1):
    suite = unittest.TestLoader().discover('.')
    runner = unittest.TextTestRunner(verbosity=verbosity)
    return runner.run(suite).wasSuccessful()

if __name__ == '__main__':
    test_all()
