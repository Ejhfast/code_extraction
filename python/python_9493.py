# django change image file location with setattr
def get_upload_to(instance, filename):
    return School._meta.get_field(instance.field_name).upload_to+"/"+filename
