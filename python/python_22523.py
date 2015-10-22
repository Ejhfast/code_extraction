# How do I exclude a string from re.findall?
if email not in self.emails and not email.endswith("png"):  # if not a duplicate
        self.csvwriter.writerow([page.title.encode('utf8'), page.url.encode("utf8"), email])
        self.emails.append(email)
