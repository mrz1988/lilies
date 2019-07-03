import unittest

def test_all(verbosity=1):
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    test_all()
