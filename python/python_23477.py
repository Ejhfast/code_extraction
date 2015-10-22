# How do I access values from python social auth used in template
from django.core.urlresolvers import reverse
twitterpath = reverse('social:begin', args=('twitter',))
