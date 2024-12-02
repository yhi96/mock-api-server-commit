import psycopg2
import pytest
from psycopg2 import OperationalError
import os
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


# Tests only run in the actual mock-db-server
@pytest.fixture(scope="module")
def db_connection():
    
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    yield conn
    conn.close()

@pytest.fixture
def db_cursor(db_connection):
    
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()

def test_connection(db_connection):
    
    assert db_connection is not None, "Could not connect to the database."

def test_retrieve_top10_expensive_products(db_cursor):

    query = """
    SELECT product_name, unit_price
    FROM products
    ORDER BY unit_price DESC
    LIMIT 10;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    assert len(results) == 10, f"Results count is not as expected, instead is {len(results)}"


def test_sum_freight_by_employee(db_connection):

    query = """
    SELECT employee_id, SUM(freight)
    FROM orders
    GROUP BY employee_id;
    """
    cursor = db_connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    expected_result = [
        (8, 7487.8804),
        (7, 6665.4404),
        (9, 3326.2598),
        (1, 8836.639),
        (5, 3918.7104),
        (2, 8696.408),
        (4, 11346.138),
        (6, 3780.4695)
    ]

    assert result == expected_result, f"Expected {expected_result}, but got {result}"
    
    cursor.close()
    # The test returns one additional result, instead of all these in expected_result which were received during execution of the
    # queries through psql. The additional result is unexpected, therefore I will consider this a bug.
    
def test_avg_max_min_age_london(db_connection):

    query = """
    SELECT city,
      AVG(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))),
      MAX(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))),
      MIN(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)))
    FROM employees
    WHERE city = 'London'
    GROUP BY city;
    """
    cursor = db_connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    expected_result = [
        ('London', 63.0000000000000000, 69, 58)
    ]

    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    cursor.close()

def test_avg_age_above_60_by_city(db_connection):

    query = """
    SELECT city, AVG(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))) AS avg_age
    FROM employees
    GROUP BY city
    HAVING EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)) > 60;
    """

    try:
       
       db_cursor = db_connection.cursor()
       db_cursor.execute(query)
       result = db_cursor.fetchall()

       assert result, "No results returned"
       
       db_connection.commit()

    except Exception as e:
       
       db_connection.rollback()
       assert False, f"Error: {e}"

    finally:

        db_cursor.close()
    # Does not return any result, only an error.
    

def test_top_3_oldest_employees(db_connection):

    query = """
    SELECT first_name, last_name, EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)) AS age
    FROM employees
    ORDER BY age DESC
    LIMIT 3;
    """

    cursor = db_connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    expected_result = [
        ('Margaret', 'Peacock', 87),
        ('Nancy', 'Davolio', 75),
        ('Andrew', 'Fuller', 72)
    ]

    assert result == expected_result, f"Expected {expected_result}, but got {result}"
    
    cursor.close()
