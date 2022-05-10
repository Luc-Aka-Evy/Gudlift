import pytest
from .conftest import client


def test_should_purchase_places(client):
    club = "She Lifts"
    competition = "Fall Classic"
    email = 'kate@shelifts.co.uk'
    client.post('/showSummary', data={'email': email})
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 5})
    assert "Great-booking complete!" in response.text
    assert response.status_code == 200
    

def test_should_not_purchase_places(client):
    club = "She Lifts"
    competition = "Fall Classic"
    email = 'kate@shelifts.co.uk'
    client.post('/showSummary', data={'email': email})
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 14})
    assert "Something went wrong" in response.text
    assert response.status_code == 200