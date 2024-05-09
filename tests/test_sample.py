import pytest
from src import sample


def test_Chatbot1():
    chatbot = sample.Chatbot()
    res = chatbot.get_response("おはよう")
    assert res == "おはようございます。"

def test_Chatbot2():
    chatbot = sample.Chatbot()
    res = chatbot.get_response("こんにちは")
    assert res == "こんにちは。"

def test_Chatbot3():
    chatbot = sample.Chatbot()
    res = chatbot.get_response("こんばんは")
    assert res == "こんばんは。"

def test_Chatbot4():
    chatbot = sample.Chatbot()
    with pytest.raises(Exception) as e:
        res = chatbot.get_response("異常値を入力")
    assert str(e.value) == "予期しない入力値です。"