import pandas as pd # type: ignore

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
