# Django: Problem reading multi valued POST variable
prices = request.POST.getlist("IPN_PRICE[]")
