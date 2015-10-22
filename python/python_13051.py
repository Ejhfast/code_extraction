# python read complex xml with ElementTree
for listInvoice in root.findall('.//{http://www.stormware.cz/schema/version_2/invoice.xsd}invoiceHeader'):
    invoiceHeader = listInvoice.find('.//{http://www.stormware.cz/schema/version_2/invoice.xsd}id').text
    print invoiceHeader
