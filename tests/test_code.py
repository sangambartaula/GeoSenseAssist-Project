import subprocess
import time
import requests
from website import create_app
def test_api_status():
    try:
        app = create_app()
        time.sleep(10)
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
    except requests.exceptions.ConnectionError as e:
        print("Connection Error:", e)
        assert False  # Force test to fail with an error message

