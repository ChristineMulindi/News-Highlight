import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(
            'Jonathan Shieber', 'Bitcoin has surged above $8,000 and theories around why abound', 'Bitcoin is now trading at around $8,130, up a whopping 60.84 percent over the past month, with the price surging $3,086.14 over the period.', ' "http://techcrunch.com/2019/05/14/bitcoin-shrug-emoji/', '"https://techcrunch.com/wp-content/uploads/2017/11/bitcoin-8000.png?w=711', '2019-05-14T14:01:21Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Articles))

