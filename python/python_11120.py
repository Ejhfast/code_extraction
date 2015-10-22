# Force YAML values to be strings
&gt;&gt; import yaml
&gt;&gt; yaml.load('string: 01', Loader=yaml.loader.BaseLoader)
{u'string': u'01'}
