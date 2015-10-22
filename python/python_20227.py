# AWS boto: how to get a list of all Internet gateways attached to a VPC
gws = conn.get_all_internet_gateways(filters={'attachment.vpc-id': vpc.id})
