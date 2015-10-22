# customize tastypie patch_list
def alter_list_data_to_serialize(self, request, data):
    #call external procedure here
    return data
