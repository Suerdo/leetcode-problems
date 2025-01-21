import pandas as pd  # type: ignore

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns = {'id' : 'student_id', 'first' : 'first_name', 'last' : 'last_name', 'age' : 'age_in_years'}) 