import pytest
from .conftest import client


def test_should_logout(client):
    email = 'kate@shelifts.co.uk'
    client.post('/showSummary', data={'email': email})
    response = client.get('/logout')
    assert response.status_code == 302