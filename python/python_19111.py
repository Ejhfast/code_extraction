# What is the proper way of saving data to an embedded document using Mongoengine and Pyramid?
self.context.job_history = [Job_history(job_title=j, from_=f, to_=t) for j,f,t in zip(job_title_list, from_list, to_list)]
