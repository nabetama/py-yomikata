# -*- coding: utf-8 -*-
from __future__ import print_function
import requests
import lxml.html


class Yomikata(object):
    def __init__(self, word=None):
        if not word:
            raise NoSearchWordError
        self._word = word
        self.get_yomikata()

    def get_yomikata(self):
        resp = requests.get("http://Yomikata.org/word/" + self.word)
        if resp.status_code != 200:
            raise Exception("Http status is not OK.")
        if not resp.text.count(self.word):
            print(u"The way to read of the word wasn't found.".format(self.word))
            return None
        html = lxml.html.fromstring(resp.text)
        answers = html.cssselect(".spAns")
        for answer in answers:
            print(u"{}: ({})".format(*self.text_and_points(answer)))

    def text_and_points(self, answer):
        ans = answer.cssselect('.psAns')
        point = answer.cssselect('.psPt')
        if ans and point:
            return ans[0].text_content(), point[0].text_content()
        return []

    @property
    def word(self):
        return self._word

class NoSearchWordError(Exception):
    pass
