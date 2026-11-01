import pytest

@pytest.fixture
def user_data():
   return {
      "name":"admin",
      "password":"1234"
   }

def test_username(user_data):
   assert user_data["name"] == "admin"

def test_password(user_data):
   assert len(user_data["password"]) > 0
