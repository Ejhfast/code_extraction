# Non-greedy matching in webapp2 routes?
webapp2.Route('/edit/([^/]+)/([^/]+)', handler = 'grouploader.Editor');
webapp2.Route('/([^/]+)/([^/]+)', grouploader.Loader);
