# Django: No of Instances of a Foreign Key
def num_of_choices(question):
    return question.choice_set.count()
