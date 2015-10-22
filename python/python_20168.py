# Item visible in browser not collected by scraper
url = "http://action.sumofus.org/api/ak_action_count_by_action/?action=nhs-patient-corporations&amp;additional="
number = int(requests.get(url).text)
