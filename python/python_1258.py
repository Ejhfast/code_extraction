# How do I update an already existing row when using ModelForms?
&gt;&gt;&gt; article = Article.objects.get(pk=1)
&gt;&gt;&gt; form = ArticleForm(instance=article)
