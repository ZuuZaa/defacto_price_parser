import unittest
import helper_def
from parser import link
from headers import headers


class TestFindAllLinks(unittest.TestCase):

    def test_links(self):
        result = helper_def.find_all_links(link,headers, 'nav','mainmenu')
        self.assertIsInstance(result, list)

