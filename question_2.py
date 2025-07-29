""".A bank has 300 employees. Each employee has a unique ID and works in one of three departments: "Finance", "IT", or "HR". Every month, the bank needs to process salaries for all employees.
Each employee has:
    A fixed monthly base salary
    A list of work logs, each containing:
        date (e.g., "2025-07-01")
        hours_worked (float)

Here are the rules for salary computation:
    If total hours_worked in the month exceeds 160 hours, they are paid 1.5x their base hourly rate for overtime hours.
    Employees in the "IT" department receive a 5% bonus if they worked more than 180 hours.
    Employees in the "Finance" department are capped at a maximum of 180 billable hours.
    Employees in "HR" do not receive overtime, regardless of hours worked.
    
INPUT"""
employees = [
    {
        "id": 101,
        "department": "IT",
        "base_salary": 4800,
        "work_logs": [
            {"date": "2025-07-01", "hours_worked": 8},
            {"date": "2025-07-02", "hours_worked": 9},
            ...
        ]
    },
    ...
]

"OUTPUT"
# Output
{
    101: 5040.0,  # base 4800 + 5% bonus = 5040 (IT bonus only)
    102: 6000.0   # base salary, hours capped at 180 = no change
}