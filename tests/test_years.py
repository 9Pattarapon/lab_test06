from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app
# import datetime

# now = datetime.datetime.now()
client = TestClient(app)

def test_test_input_year_api():
    input = "2540"
    output = 25
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_test_input_zero_api():
    input = "0"
    output = "years not less than 0"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_test_year_unable_calculate_api():
    input = "2566"
    output = "unable to calculate"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_test_year_Underflow_api():
    input = "-99"
    output = "years not less than 0"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

   