# Filter Queryset by field in OnetoOne model
queryset = Model.objects.order_by('modelextended__author').distinct('modelextended__author')
