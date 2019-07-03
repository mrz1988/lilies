import unittest

def test_all():
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    test_all()
