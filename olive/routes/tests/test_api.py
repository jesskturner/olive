from application import app


def test_api_health_check_returns_ok():
    request, response = app.test_client.get('/api/_health_check')
    assert response.status == 200


def test_api_meta_returns_ok():
    request, response = app.test_client.get('/api')
    assert response.status == 200
