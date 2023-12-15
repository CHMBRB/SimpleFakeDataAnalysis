#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
from .db import root_dir
from .db import engine
# from pathlib import Path
# from sqlalchemy import create_engine


# # define the connection string
# db_connection_string = "sqlite:///../data/sqlite.db"

# # instantiate application database connection for 'sql_kwargs'
# engine = create_engine(db_connection_string)

# variable to determine if our root directory; ternary assignment
# NOTE: There's a reason for this. The actual Root project, ie. Where the Pipfile is located (where users would start an ipython session) is a directory level above where our Jupyter notebooks will be accessing the same directories
# root_dir = Path("../data/") if Path("../data/").exists() else Path("./data/")


# declare a dictionary object to store (most) of our global constant variables
# initial usage will be explicit within context, but this object will minimize redundancies: I REPEAT -> DRY (Don't Repeat Yourself!)
# TODO: review
CONSTANT = {
    # Files, Directories, & Other Static Resources
    # "connection_string": "sqlite:///../data/sqlite.db",
    "spreadsheet": root_dir.joinpath("Spreadsheet.xlsx"),
    "data_dir": root_dir,

    # CSV Related items
    # """
    #     # this code doesn't conform with PEP (The Python Code Standards Formatting Definition Committee)
    #     # the intent is to demonstrate a direct comparison with C# LINQ/FluentAPI and SQL for familiar users.
    #     # this comment syntax doesn't comply either (As a matter of preference I would suggest the use of the pre-commit library to make code conform to development team "standards")
    #     # PS. there are linters available for almost every language.  =)
    # """
    # get a list of csvs for accessing/loading into DataFrames with Pandas
    # (hint: if they're missing then they're generated using the SimpleFakeDataUtility repository)
    # bonus points: ternary statement in python; let's refactor to cut down on the key count (thus root_dir was born)
    # old version
    # "csv_list": [
    #     f for f
    #     in Path("../data/").iterdir()
    #     if str(f).endswith('.csv') 
    #         and str(f) != '../data/Person1.csv' 
    # ] if Path("../data/").exists() else [
    #     f for f
    #     in Path("./data/").iterdir()
    #     if str(f).endswith('.csv')
    #         and str(f) != '../data/Person1.csv' 
    # ],

    # refactored version

    "csv_list": [
        f for f
        in root_dir.iterdir()
        if str(f).endswith('.csv') 
            and str(f) != str(root_dir.joinpath('Person1.csv')) 
    ],

    # store and unpack our 'csv' arguments using **kwargs
    "csv_kwargs": {
        'sep': "\t",
        'index_col': "id",
        'low_memory': False,
    },

    # SQL Queries
    # this query reflects a general SQL JOIN statement to get ALL of the data at once
    "sql_query": """
        SELECT *
        FROM persons p
        JOIN contactdetails c
            ON p.id == c.id
        JOIN labordetails l
            ON p.id == l.person_id;
    """,

    # additional SQL kwargs (see 'csv_kwargs' above)
    "sql_write_kwargs": {
        "if_exists": "replace",
        "index_label": "id",
        "con": engine,
    },
    "sql_kwargs": {
        "con": engine,
    },

    # common columns to restrict df from payroll data
    # MUST drop_duplicates(inplace=True) & reset_index(inplace=True, drop=True)
    "cols": [
        'lname',
        'fname',
        'email',
        'address',
        'city',
        'state',
        'zipcode',
        'dob',
        'payrate',
    ],

    # 'na mea
    "url": (
        "https://raw.githubusercontent.com/pandas-dev"
        "/pandas/main/pandas/tests/io/data/csv/tips.csv"
    )

}

# declare a sqlite file database connection (alternative if you REALLY want to type more by including con=engine in pandas read/write operations)
# otherwise, we'll unpack additional args via: **CONTANT.get('sql_kwargs')
# engine = create_engine(CONSTANT.get('connection_string'))