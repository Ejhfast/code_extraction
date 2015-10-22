# Checking for duplicates
value = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status', unique=True)
