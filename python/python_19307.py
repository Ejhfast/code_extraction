# Flask project works in local environment, throws weird error on heroku about missing files (that are dynamically added anyway!)
if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)
