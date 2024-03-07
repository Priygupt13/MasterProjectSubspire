def add_data(self, question: str, **kwargs) -> str:
    """
    **Example:**
    ```python
    vn.generate_sql_from_question(question="What is the average salary of employees?")
    # SELECT AVG(salary) FROM employees
    ```

    Generate an SQL query using the Vanna.AI API.

    Args:
        question (str): The question to generate an SQL query for.

    Returns:
        str or None: The SQL query, or None if an error occurred.
    """
    params = [Question(question=question)]

    d = self._rpc_call(method="generate_sql_from_question", params=params)

    if "result" not in d:
        return None

    # Load the result into a dataclass
    sql_answer = SQLAnswer(**d["result"])
    if "No SELECT statement" in sql_answer.sql:
        return sql_answer.raw_answer
    else:
        return sql_answer.sql
