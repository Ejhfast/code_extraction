# openerp cutomer tree view
'partref_id': fields.many2one('res.partner', 'Related Company'),
'ref_partner_ids': fields.one2many('res.partner', 'partref_id', 'Refrence partner'),
