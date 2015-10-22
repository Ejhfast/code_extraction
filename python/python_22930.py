# python - memory error
with open('list.txt') as f:
    total = sum(block.count('\n')
                for block in iter(lambda: f.read(64*1024), ''))
