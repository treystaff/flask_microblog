#!flask/bin/python
# Convenience script for migrating the db
import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
import os

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = os.path.join(SQLALCHEMY_MIGRATE_REPO,
                         'versions/{0}_migration.py'.format(str(v+1).zfill(3)))


tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta, db.metadata)
open(migration, 'wt').write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('new migration saved as ' + migration)
print('Current database version: ' + str(v))
