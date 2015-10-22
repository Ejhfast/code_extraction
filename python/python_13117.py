# Updating a embedded documents in mongoengine
Feed.objects(_id="...", posts__text="findvalue").update(set__posts__S__value="updatevalue")
