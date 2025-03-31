import xml.etree.ElementTree as ET
from lxml import etree  # This is for XML validation against XSD schema (optional)

# Function to get user input and generate XML
def generate_xml():
    # Collect user inputs
    username = input("Enter username (8-12 characters): ")
    post = input("Enter post (5-8 characters): ")
    salary = input("Enter salary: ")
    gender = input("Enter gender (Male, Female, Other): ")
    temporary = input("Enter temporary address: ")
    permanent = input("Enter permanent address: ")
    password = input("Enter password (6-15 characters): ")

    # Create the root element <Butwal>
    root = ET.Element("Butwal")
    
    # Create <employee> element as a child of root
    employee = ET.SubElement(root, "employee")
    
    # Add child elements to <employee>
    ET.SubElement(employee, "username").text = username
    ET.SubElement(employee, "post").text = post
    ET.SubElement(employee, "salary").text = salary
    ET.SubElement(employee, "gender").text = gender
    address = ET.SubElement(employee, "address")
    ET.SubElement(address, "temporary").text = temporary
    ET.SubElement(address, "permanent").text = permanent
    ET.SubElement(employee, "password").text = password
    
    # Add <ID> element at root level
    ET.SubElement(root, "ID").text = "12345"

    # Generate XML file and save it
    tree = ET.ElementTree(root)
    tree.write("user_data.xml")

    print("XML file 'user_data.xml' has been generated.")

    # OPTIONAL: Validate XML against XSD Schema
    validate_xml()

# Function to validate XML file using an XSD schema (if needed)
def validate_xml():
    try:
        # Load and parse the schema (XSD) file
        schema_doc = etree.parse("schema.xsd")
        schema = etree.XMLSchema(schema_doc)
        
        # Load and parse the generated XML file
        xml_doc = etree.parse("user_data.xml")
        
        # Validate the XML document
        schema.assertValid(xml_doc)
        print("XML file is valid according to the XSD schema.")
    except etree.XMLSchemaError as e:
        print(f"XML is invalid: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
generate_xml()
