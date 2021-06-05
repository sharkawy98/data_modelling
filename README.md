# PostgreSQL data modelling project from Udacity DE nanodegree

### Here is the generated star schema of the data collected from JSON files:
![star_schema](https://user-images.githubusercontent.com/36075516/119294862-ba5f9380-bc55-11eb-85c0-e4cfaa5cfcb6.png)

### Description of what each file is doing:

* `test.ipynb` displays few rows of each table to validate the work done.
* `create_tables.py` drops and creates the tables, to rest the tables if you want.
* `etl.py` reads and processes all files from song_data and log_data and loads them into the tables.
* `sql_queries.py` contains all sql queries, and is imported into the last three files above.
