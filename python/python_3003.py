# need help optimizing a geo algorithm using a map() operation, lists, floats and some validation
approved_rides = [ride for ride in initial_rides if any(
          (lat_min &lt; step.latitude&lt; lat_max and \
           lng_min&lt; step.longitude&lt; lng_max) for step in ride.route.steps.all())]
