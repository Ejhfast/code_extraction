# Add space between commas if it is not a number
re.sub(r"(?&lt;![\d])(,+)(?![\d])", r' \g&lt;1&gt; ', sentence)
