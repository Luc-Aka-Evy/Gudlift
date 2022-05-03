from http import server
from urllib import response
import pytest


from conftest import client


def test_should_fail_with_unknow_email(client):
    email = 'fake@test.com'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 500
    

def test_should_pass_with_register_email(client):
    email = 'john@simplylift.co'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200

