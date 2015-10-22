# Django query - Retrieve objects that don't have other object pointing to them
String.objects.filter( language = 'english',
                       string__original_string__isnull = True )
