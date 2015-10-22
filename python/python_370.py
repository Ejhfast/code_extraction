# Debugging IronPython scripts in hosted (embedded) environment
Dictionary&lt;string, object&gt; options = new Dictionary&lt;string, object&gt;();
        options["Debug"] = true;
        engine = Python.CreateEngine(options);
