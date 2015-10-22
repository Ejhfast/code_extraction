# Check which branches contain a specific git commit sha using Python dulwich?
branches = [ref for ref in repo.refs.keys("refs/heads/") if
            any((True for commit in repo.get_walker(include=[repo.refs[ref]])
                 if commit.id == YOURSHA))]
