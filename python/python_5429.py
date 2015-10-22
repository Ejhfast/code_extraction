# Self-referential Queries in Django
from django.db.models import F
StockRequest.objects.filter(amount_requested=F("amount_approved"))
