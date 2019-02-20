from io import StringIO
from lxml import etree

class HtmlParser():
    def __init__(self):
        self.parser = etree.HTMLParser()

    def parse(self, html):
        tree = etree.parse(StringIO(html), parser=self.parser)
        h3s = tree.getroot().findall(".//h3")
        return h3s[7].text

    def parse_error(self, html):
        tree = etree.parse(StringIO(html), parser=self.parser)
        spans = tree.getroot().findall(".//span")
        return spans[12].text
