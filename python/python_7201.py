# Order a queryset in django by an annotated field and append the rest of the objects that did not fit the criteria
new_queryset = one_queryset | second_queryset
