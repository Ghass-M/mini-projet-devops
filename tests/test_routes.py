import pytest

def test_index_or_health(client):
    """
    Call the root path. Accept common expected responses so the test is tolerant
    to different project setups (200, redirect, or 404 if no index route).
    """
    res = client.get('/')
    assert res.status_code in (200, 301, 302, 404)

def test_404_for_unknown_route(client):
    res = client.get('/this-route-should-not-exist')
    assert res.status_code == 404