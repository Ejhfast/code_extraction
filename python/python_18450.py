# How to update a single column in a subset of database table records using Django form or ModelForm?
verifications = Verification.objects.filter(asset_code__range=(10, 100))
verifications.update(product_details=form.cleaned['product_details'])
