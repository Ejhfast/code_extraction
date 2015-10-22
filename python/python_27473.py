# How to integrate sendgrid templates with python app?`
message = sendgrid.Mail()
message.add_filter('templates', 'enable', '1')
message.add_filter('templates', 'template_id', 'TEMPLATE-ALPHA-NUMERIC-ID')
