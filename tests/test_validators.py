
import pytest

from source.validators import validate_name,validate_email,validate_salary,validate_department,validate_joining_date,validate_status,validate_employee_data
from source.exceptions import ValidationError

def test_valid_name():
    """Test successful name validation"""
    assert validate_name("rajesh")

def test_invalid_name():
    """Test name validation with invalid input"""
    with pytest.raises(ValidationError):
        validate_name("")

def test_valid_email():
    """Test successful email validation"""
    assert validate_email("rajesh123@gmail.com")

def test_invalid_email():
    """Test email validation with invalid input"""
    with pytest.raises(ValidationError):
        validate_email("rajesh123gmail.com")

def test_valid_salary():
    """Test successful salary validation"""
    assert validate_salary("2300")

def test_invalid_salary():
    """Test salary validation with invalid salary"""
    with pytest.raises(ValidationError):
        validate_salary("-100")

def test_valid_department():
    """Test successful deparment validation"""
    assert validate_department("IT")

def test_invalid_department():
    """Test department validation with invalid deparment"""
    with pytest.raises(ValidationError):
        validate_department("Marketing")

def test_valid_joiningdata():
    """Test successful joining data validation"""
    assert validate_joining_date("2026-10-22")
@pytest.mark.xfail()
def test_invalid_joiningdata():
    """Test joining data validation with invalid joining data"""
    with pytest.raises(ValidationError) :                              
        validate_joining_date("22-10-2003")
@pytest.mark.status()
def test_valid_status():
    """Test successful status validation"""
    assert validate_status("Active")
@pytest.mark.status()
def test_invalid_status():
    """Test name validation with invalid input"""
    with pytest.raises(ValidationError):
        validate_status("inactive")


def test_valid_employee_data():
    """Test successful employee data validation"""
    employee = {
        "name": "Rajesh",
        "email": "rajesh@gmail.com",
        "department": "IT",
        "salary": "25000.0",
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    assert validate_employee_data(employee) 


def test_invalid_employee_data():
    """Test employee data validation with invalid name"""
    employee = {
        "name": "",
        "email": "rajesh@gmail.com",
        "department": "IT",
        "salary": 25000,
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    with pytest.raises(ValidationError):
        validate_employee_data(employee)
       
