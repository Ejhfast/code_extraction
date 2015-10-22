# How does sklearn random forest index feature_importances_
importances = rf.feature_importances_
important_names = feature_names[importances &gt; np.mean(importances)]
print important_names
