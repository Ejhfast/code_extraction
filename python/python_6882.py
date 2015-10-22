# Adding radio buttons to customised form in web2py
db.payment_bpay_step1.selection_type.widget = \
    lambda f, v: SQLFORM.widgets.radio.widget(f, v, style='divs')
