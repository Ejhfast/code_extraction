# api_limit_status().remaininghits key ERROR ; Script Not Working; Cannot fetch friends
limits = api.rate_limit_status()
remain_search_limits = limits['resources']['search']['/search/tweets']['remaining']
