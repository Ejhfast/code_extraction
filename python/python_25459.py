# what can i use form.cleaned_data in my to query a database?
que = form.cleaned_data['question']
x = QuestionModel.objects.get(question=que)
