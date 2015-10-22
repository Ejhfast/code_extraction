# graphviz cluster's label multiple lines
router_label="&lt;"+router_name+"&lt;BR /&gt;"+router_ip+"&gt;"
c = gv.Graph(cluster_name)
c.body.append('label='+router_label)
