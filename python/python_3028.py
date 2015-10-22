# mongodb union $or problems
find = self.db.action_log.find()
find.where(pymongo.code.Code('this.dest_id==1 || this.src_id==2'))
