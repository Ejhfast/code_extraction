# Can keys be rearranges after dictionary creation?
sorted(x.items(), key=lambda t: -len(t[1]))
# [('THREE', ['up', 'side', 'down']), ('TWO', ['hot', 'mess']), ('ONE', ['foo'])]
