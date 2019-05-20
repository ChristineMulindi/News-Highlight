import unittest
from app.models import Source



class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(
            'cnn', 'CNN', 'In Tehran, specter of war met with more defiance than fear - CNN', 'https://abcnews.go.com', 'general', 'no')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))



