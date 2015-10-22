# Django Forms Default Select Value in Front of Dynamic Loop
payment = forms.ChoiceField(required=True, label='Type',
                            choices=[(None, 'Select Type')]+card_choices)
