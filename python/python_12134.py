# cloudinary cloudinary.models.CloudinaryField add public_id to the field
class MyCloudinaryField(CloudinaryField):
    def upload_options(self, model_instance):
       return {'public_id': model_instance.supplier.user.id + "-" + model_instance.designNumber}
