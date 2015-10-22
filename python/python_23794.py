# Labels with list in matplotlib
for x_entry, y_entry, label in zip(x,y,labels):
        print label
        self.map.plot(x_entry, y_entry, 'bo', markersize=10, picker=5, label=label)
