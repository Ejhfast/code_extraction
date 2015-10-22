# Calculate average values from an array
average_temps_array = [sum(map(float, hourly_temp[i:i+24])) / 24
                                 for i in range(0, len(hourly_temp), 24)]
