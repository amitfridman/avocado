from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from avocados.views import avocado_predict
from rest_framework import status
import datetime
from django.utils import timezone
import pytest


@pytest.fixture()
def test_json_valid():
    test_json = [{
            "total_volume": 64236.62,
            "t_4046": 1036.74,
            "t_4225": 54454.85,
            "t_4770": 48.16,
            "total_bags": 8696.87,
            "small_bags": 8603.62,
            "large_bags": 93.25,
            "x_large_bags": 0.0,
            "type": "conventional",
            "year": 2015,
            "region": "New York"
        },
        {
            "total_volume": 64236.62,
            "t_4046": 1036.74,
            "t_4225": 54454.85,
            "t_4770": 48.16,
            "total_bags": 8696.87,
            "small_bags": 8603.62,
            "large_bags": 93.25,
            "x_large_bags": 0.0,
            "type": "organic",
            "year": 2015,
            "region": "Los Angeles"
        },
        {
            "total_volume": 64236.62,
            "t_4046": 1036.74,
            "t_4225": 54454.85,
            "t_4770": 48.16,
            "total_bags": 8696.87,
            "small_bags": 8603.62,
            "large_bags": 93.25,
            "x_large_bags": 0.0,
            "type": "organic",
            "year": 1990,
            "region": "Los Angeles"
        },
    ]
    return test_json


@pytest.fixture()
def test_json_invalid():
    test_json = [
        {
            "total_volume": 64236.62,
            "t_4046": 1036.74,
            "t_4225": 54454.85,
            "t_4770": 48.16,
            "total_bags": 8696.87,
            "small_bags": 8603.62,
            "large_bags": 93.25,
            "x_large_bags": 0.0,
            "type": "conventional",
            "year": 15,
            "region": "Albany"
        },
        {
            "total_volume": 64236.62,
            "t_4046": 1036.74,
            "t_4225": 54454.85,
            "t_4770": 48.16,
            "total_bags": 8697.87,
            "small_bags": 8603.62,
            "large_bags": 93.25,
            "x_large_bags": 0.0,
            "type": "conventional",
            "year": 2015,
            "region": "Baltimore"
        },
        {
            "total_volume": 64236.62,
            "t_4046": 1036.74,
            "t_4225": 54454.85,
            "t_4770": 48.16,
            "total_bags": 8696.87,
            "small_bags": 8603.62,
            "large_bags": 93.25,
            "x_large_bags": 0.0,
            "type": "garbage",
            "year": 2015,
            "region": "Los Angeles"
        },
    ]
    return test_json


@pytest.mark.django_db
def test_valid(test_json_valid):
    factory = APIRequestFactory()

    for test in test_json_valid:
        request = factory.post('/avocados/', test, format='json')
        response = avocado_predict(request)
        assert response.status_code == status.HTTP_200_OK, "failed"

@pytest.mark.django_db
def test_invalid(test_json_invalid):
    factory = APIRequestFactory()
    for test in test_json_invalid:
        request = factory.post('/avocados/', test, format='json')
        response = avocado_predict(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST, "created successfully although it" \
                                                                    " wasn't supposed to"



