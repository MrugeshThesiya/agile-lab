import pytest

@pytest.mark.great
def test_greater():
   num = 100
   assert num > 50

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.less
def test_less():
   num = 100
   assert num < 200

@pytest.mark.less
def test_pass():
   num = 100
   assert num > 50
