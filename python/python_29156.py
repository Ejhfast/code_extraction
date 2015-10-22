# How to generate tuples of (original lable, predicted label) on Spark with MLlib?
predictions = model.predict(parsedTrainData.map(lambda x: x.features))
labelsAndPredictions = parsedTrainData.map(lambda x: x.label).zip(predictions)
