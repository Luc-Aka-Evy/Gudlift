import pytest
from .conftest import client


def test_should_check_booking_places_in_past_competition(client):
    email = 'john@simplylift.co'
    response = client.post('/showSummary',data={'email': email})
    assert response.status_code == 200
    assert "This competition is over" in response.text
    assert "Book Places" in response.text