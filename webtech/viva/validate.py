import xmlschema

xml_file = "rec.xml"
xsd_file = "rec.xsd"


schema = xmlschema.XMLSchema(xsd_file)


if schema.is_valid(xml_file):
    print(" XML is valid according to the schema!")
else:
    print(" XML is NOT valid!")
    
    
    for error in schema.iter_errors(xml_file):
        print(f"Error: {error}")
