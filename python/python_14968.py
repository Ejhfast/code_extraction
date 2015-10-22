# Django: Getting image urls as list
urls_list = [MEDIA_URL + image_path for image_path in SampleModel.objects.values_list('imageFieldObj', flat=True)]
