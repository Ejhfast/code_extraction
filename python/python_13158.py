# Swap position of entities in the list
&gt;&gt;&gt; x = [['True_304', 'false_2'], ['True_702', 'false_2_1'], ['True_204', 'false_222_2']]
&gt;&gt;&gt; [[b, a] for [a, b] in x]
[['false_2', 'True_304'], ['false_2_1', 'True_702'], ['false_222_2', 'True_204']]
