from employee import employee_details

def test_employee_details_Rahul():
    result = employee_details("Rahul", 101, "IT", 50000)
    expected = "Employee Name: Rahul, Employee ID: 101, Department: IT, Salary: 50000"
    assert result == expected