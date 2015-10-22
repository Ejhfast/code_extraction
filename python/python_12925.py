# Is possible to create Column in SQLAlchemy which is going to be automatically populated with time when it inserted/updated last time?
last_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
