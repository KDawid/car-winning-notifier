from html_parser import HtmlParser
from web_caller import WebCaller

NOT_WON_TEXT = 'Sajnos, az Ön által megadott %s sorszámú gépkocsinyeremény betét nem nyert. '
ERROR_TEXT = 'A sorszám kizárólag 9 számjegyet tartalmazhat!'

NUMBERS = ['123456788', '133311367', '666666666', '66661666']

caller = WebCaller()
parser = HtmlParser()

for number in NUMBERS:
    print("Checking number %s" % number)
    html = caller.get_content(number)
    if (NOT_WON_TEXT % number) == parser.parse(html):
        print("\t%s not won" % number)
    elif ERROR_TEXT == parser.parse_error(html):
        print("\t%s seems not to be valid number - is its length 9?" % number)
    else:
        print("\tThere is a chance that %s has won, sending e-mail" % number)

