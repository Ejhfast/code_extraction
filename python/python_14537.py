# Django How to find out if earlier than 7pm in a specific timezone
tz = timezone('US/Eastern')
datetime.now(timezone(tz)).hour&lt;19
