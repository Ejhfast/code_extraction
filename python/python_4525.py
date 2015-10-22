# python mongodb regex: ignore case
import re
config.gThingCollection.find({"name": re.compile(regex, re.IGNORECASE)})
