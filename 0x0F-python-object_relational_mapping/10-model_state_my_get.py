#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name name.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    # Check if the number of arguments is correct
    if len(sys.argv) != 5:
        print('Usage: argv[0] <username> <password> <database>',
              file=sys.stderr)
        exit()

    # Create a SQLAlchemy engine that provides a source of database
    # connectivity
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],  # username
            sys.argv[2],  # password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True
    )

    # Create all tables in the engine ("Base.metadata.create_all" is akin to
    # "CREATE TABLE" statement in raw SQL)
    Base.metadata.create_all(engine)

    # Create a new session
    session = Session(engine)

    # Query the State table
    states_table = session.query(State).all()
    found = False
    for state in states_table:
        if state.name == sys.argv[4]:
            found = True
            print(state.id)
            break
    if not found:
        print('Not found')

    # Close the session
    session.close()
