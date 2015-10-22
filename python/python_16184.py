# remove tag and contents based on child tag value - python lxml
for crew in root.xpath('.//crew[descendant::role[contains(text(), "Primary")]]'):
    crew.getparent().remove(crew)
