# Add content inside html body tag
soup = BeautifulSoup(your_old_html)
soup.body.insert(0, your_tag)
print soup
