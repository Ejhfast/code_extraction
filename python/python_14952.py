# OpenERP ver 7 Domain filter with more conditions
'work_offers_id':fields.many2one('bpl.work.offer', 'Work Offer', domain="['&amp;',('bpl_company_id','=',bpl_company_id),('bpl_estate_id','=',bpl_estate_id),'&amp;',('bpl_division_id','=',bpl_division_id),'|',('gang_no','=',gang_no),('date_of_offer','=',offered_date)]"),
