import os
import requests


def test_proxyspec():
    url = os.environ.get("SHINYPROXY_URL", "http://shiny.test:8000")
    r = requests.get(f"{url}/api/proxyspec")
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_spawn():
    url = os.environ.get("SHINYPROXY_URL", "http://shiny.test:8000")
    r = requests.post(f"{url}/api/proxy/01_hello")
    assert r.status_code == 201
    assert r.json().get("status") == "Up"
