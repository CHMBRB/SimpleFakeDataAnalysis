from sqlalchemy import create_engine
from pathlib import Path

# variable to determine if our root directory; ternary assignment
# NOTE: There's a reason for this. The actual Root project, ie. Where the Pipfile is located (where users would start an ipython session) is a directory level above where our Jupyter notebooks will be accessing the same directories
root_dir = Path("../data/") if Path("../data/").exists() else Path("./data/")

# define the connection string
# db_connection_string = "sqlite:///../data/sqlite.db"
db_connection_string = f"sqlite:///{root_dir}/sqlite.db"

# instantiate application database connection for 'sql_kwargs'
engine = create_engine(db_connection_string)



## TODO: Evaluate likelihood of using a user-defined database connection outside of our CONSTANT definitions in .globals file

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # an Engine, which the Session will use for connection
# # resources, typically in module scope
# # engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")

# # a sessionmaker(), also in the same scope as the engine
# # Session = sessionmaker(engine)


# class Connection:
#     """Generic class for encapsulated sqlalchemy database connections"""

#     def __init__(self, connection_string):
#         self.engine = create_engine(connection_string)
#         # self.session = sessionmaker(self.engine)