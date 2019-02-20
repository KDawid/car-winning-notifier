import requests

class WebCaller():
    def get_content(self, number):
        url = "https://www.otpbank.hu/portal/hu/Megtakaritas/ForintBetetek/Gepkocsinyeremeny"
        result = requests.post(url, data={'sorszam': number})
        return str(result.content.decode("utf-8"))
