# web2py dropdown menu generate from database with main and sub categories
def menu_rec(items):
    return [(x.title,None,URL('shop', 'category',
        args=pretty_url(x.id, x.slug)), menu_rec(x.children)) for x in items or []]
