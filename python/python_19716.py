# Django JOIN with column renaming to queryset
user_choice_list = userChoice.objects.filter(questionnaire=user_questionnaire.id).values('id' , 'question_id' , 'questionnaire_id', 'question__text', 'votes', 'text')
