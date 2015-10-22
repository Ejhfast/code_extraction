# Python: sorting datetime objects keeping "AM" and "PM" into account
dates = sorted([datetime.strptime(regex_obtained_str, '%B %d, %Y, %I:%M:%S %p')
                for regex_obtained_str in strings])
l = [date.strftime('%m/%d/%Y %I:%M:%S %p') for date in dates]
