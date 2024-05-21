# Pandas8

# 1 Problem 1: Find Total Time Spent By Each Employee ( https://leetcode.com/problems/find-total-time-spent-by-each-employee/ )
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['emp_id','event_day'])['total_time'].sum().reset_index()
    return employees[['event_day','emp_id', 'total_time']].rename(columns = {'event_day': 'day'})

# 2 Problem 2 : Number of Unique Subjects Taught By Each Teacher ( https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)



# 3 Problem 3 : Classes more than 5 Students ( https://leetcode.com/problems/classes-more-than-5-students/ )


