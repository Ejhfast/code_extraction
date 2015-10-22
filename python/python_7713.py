# Why are PNG images rendered from a QGraphicsScene being incorrectly offset?
view = QGraphicsView()
view.setScene(scene)
view.setSceneRect(QRectF(view.viewport().rect()))
