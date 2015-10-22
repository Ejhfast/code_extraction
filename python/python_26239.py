# Python parsing url into dict: duplicate keys
{k: [v[0]] for k, v in parse_qs('item_type=15&amp;color=336&amp;color=45').items()}
