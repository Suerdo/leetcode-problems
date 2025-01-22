import pandas as pd # type: ignore

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student_info = students[students['student_id'] == 101][['name', 'age']]
    return student_info
