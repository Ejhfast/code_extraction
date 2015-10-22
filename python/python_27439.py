# Python SQLAlchemy and Postgress - How to query a JSON element
records = db_session.query(Resource).filter(
              Resources.data["lastname"].astext == "Doe"
          ).all()
