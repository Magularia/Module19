import pytest
from api.api_booking import get_booking_list, create_booking

def test_boooking_list():
      response  =  get_booking_list()
      assert response.status_code  ==  200

def  test_create_booking():
    response = create_booking("Test", "Test1", 123, True, "2023-06-01", "2023-06-10", "Dog")
    assert response.status_code  == 200
