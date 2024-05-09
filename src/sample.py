import datetime
import requests


class Chatbot():
    def get_response(self, request):
        greetres = GreetRes(request)
        res = greetres.get()
        return res


class GreetRes():

    def __init__(self, request):
        self.request = request

    def get(self):
        if self.request == "おはよう":
            return "おはようございます。"
        elif self.request == "こんにちは":
            return "こんにちは。"
        elif self.request == "こんばんは":
            return "こんばんは。"
        else:
            raise Exception("予期しない入力値です。")
