import requests
import pytest
import unittest.mock as mock
from pyclient import jwt_token,api_key,list_api,post,update,delete

@mock.patch("requests.post")
def test_jwt_token(mock_post):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_post.return_value = mock_resp
    data = jwt_token()
    assert data.status_code == 200
@mock.patch("requests.post")
def test_api_key(mock_get):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp
    data = api_key()
    assert data.status_code == 200
@mock.patch("requests.get")
def test_listapi(mock_get):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp
    data = list_api()
    assert data.status_code == 200
@mock.patch("requests.post")
def test_createapi(mock_get):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp
    data =post()
    assert data.status_code == 200
@mock.patch("requests.put")
def test_update(mock_get):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp
    data = update()
    assert data.status_code == 200
@mock.patch("requests.delete")
def test_delete(mock_get):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_get.return_value = mock_resp
    data = delete()
    assert data.status_code == 200