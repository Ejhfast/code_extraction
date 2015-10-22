# Django Form context data lost on validation fail
user_object = self.request.user
files = [user_object.logo]
return render_to_response('directory/business_edit.html', {'form': form, 'uploaded_files': files}, context_instance=RequestContext(request))
