# Handling a two-table join on values of two columns
CREATE INDEX idlinks_i1 ON idlinks(rebate_site_id,store_id_from_site);
CREATE INDEX rebates_i1 ON rebates(rebate_site_id,store_id_from_site);
