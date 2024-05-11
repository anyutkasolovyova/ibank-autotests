from client.ibank_client import IBankClient


def test_answer():
    ibank_client = IBankClient()
    ibank_client.http_get("https://postman-echo.com/get")

    assert 1 == 1
