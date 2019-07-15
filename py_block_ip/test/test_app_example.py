import requests


def test_app():
    assert requests.get('http://127.0.0.1:3000/', timeout=1).status_code, 200
    assert requests.get('http://127.0.0.1:3000/home', timeout=1).status_code, 404
    assert requests.get('http://127.0.0.1:3000/wp-admin/index.php', timeout=1).status_code, 423


if __name__ == "__main__":
    test_app()
