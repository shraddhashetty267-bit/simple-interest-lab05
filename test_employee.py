from employee import employee_details

def test_employee_details():
    result = employee_details(
        "Rahul", 101, "IT", 30000
    )

    expected = (
        "Name: Rahul\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 30000"
    )

    assert result == expected