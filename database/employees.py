employees = {
    "john": {
        "name": "John",
        "department": "Engineering",
        "pto_days": 12
    },
    "mary": {
        "name": "Mary",
        "department": "Finance",
        "pto_days": 18
    }
}


def get_employee_pto(employee_name: str):

    employee = employees.get(
        employee_name.lower()
    )

    if not employee:
        return "Employee not found"

    return (
        f"{employee['name']} has "
        f"{employee['pto_days']} PTO days remaining."
    )
