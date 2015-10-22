# Django aggregation--find each employee's total commissions
Employee.objects.annotate(total_commission=Sum('sale__commission'))
