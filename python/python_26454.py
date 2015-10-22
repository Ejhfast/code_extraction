# how to assign current logined user to a models object in django
save_prof = comp_prof.save(commit=False)
save_prof.user = request.user
save_prof.save()
