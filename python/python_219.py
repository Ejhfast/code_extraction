# how to pass id from url to post_save_redirect in urls.py
def update_object_wrapper(request, object_id, *args, **kwargs):
    redirect_to = reverse('your object edit url name', object_id)
    return update_object(request, object_id, post_save_redirect=redirect_to, *args, **kwargs)
