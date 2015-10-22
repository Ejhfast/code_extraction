# Model.objects.filter([foreign table]).update()
Book.objects.filter(processed=True, volume__is_file_processed=True).exclude(volume__is_file_processed=False).update(status="PU")
# Or
Book.objects.exclude(volume__is_file_processed=False).filter(processed=True, volume__is_file_processed=True).update(status="PU")
