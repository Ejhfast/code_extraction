# Find XPATH with namespace and based on parent element
start_times = node.xpath("//t:chapter/start_time/text()",
                   namespaces={'t':'http://example.com/namespace'})
