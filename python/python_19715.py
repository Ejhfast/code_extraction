# Openrerp chatter message_post error
def function_which_post_msg(self, cr, uid, ids, context=None):
    self.message_post(cr, uid, [ids[0]], body=_("New Question has been &lt;b&gt;created&lt;/b&gt;"), context=context)
