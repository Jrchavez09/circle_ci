from hello import app

def test_route_hello():
    response = app.test_client().get('/')
    assert response.data == b'<p>Hello, World!</p>'
    assert response.status_code == 300
