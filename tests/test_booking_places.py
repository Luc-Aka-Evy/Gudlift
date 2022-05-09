import pytest
from conftest import client

def test_should_book_places(client):
    club = "Simply Lift"
    competition = "Spring Festival"
    email = 'john@simplylift.co'
    client.post('/showSummary', data={'email': email})
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 12})
    assert "Great-booking complete!" in response.text
    assert response.status_code == 200


def test_should_not_book_places(client):
    club = "Simply Lift"
    competition = "Spring Festival"
    email = 'john@simplylift.co'
    client.post('/showSummary', data={'email': email})
    response = client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 14})
    assert "Something went wrong" in response.text
    assert response.status_code == 200