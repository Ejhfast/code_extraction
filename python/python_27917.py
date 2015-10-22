# How to use PostgreSQL on a Pyramid App in OpenShift?
import os
engine = create_engine(os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL'))
