import pytest
from conftest import client


def test_should_get_points_display_board_page(client):
    email = 'john@simplylift.co'
    client.post('/showSummary', data={'email': email})
    response = client.get('/pointsDisplay')
    assert response.status_code == 200
    assert "Points Display board" in response.text