# how add facet to pysolr query
solrquery = "(.................. )"
solr.search([solrquery],facet = 'on' ,** {'facet.field' : ['fieldname']})
