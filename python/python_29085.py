# Django get data by one table with filtered set of related objects
OfferSite.objects.all().prefetch_related(Prefetch("offeritem_set", queryset=OfferItem.objects.filter(offer_date=tod), to_attr="offers"))
