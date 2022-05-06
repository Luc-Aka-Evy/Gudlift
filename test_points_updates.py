import pytest
from conftest import client


def test_check_points_balance_after_booking_places(client):
    club = "Simply Lift"
    competition = "Spring Festival"
    email = 'john@simplylift.co'
    client.post('/showSummary', data={'email': email})
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 12})
    assert response.status_code == 200
    assert "Points available: 1" in response.text