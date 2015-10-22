# Flask - return items to base.html
@app.context_processor
def inject_test():
    return {'test': 'Available to all'}
