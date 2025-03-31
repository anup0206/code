# import lxml.etree as ET

# xml_file = "students.xml"
# xslt_file = "transform.xsl"

# # Parse XML and XSLT files
# xml = ET.parse(xml_file)
# xslt = ET.parse(xslt_file)

# # Transform XML to HTML
# transform = ET.XSLT(xslt)
# html_output = transform(xml)

# # Save to output.html
# with open("output.html", "wb") as f:
#     f.write(ET.tostring(html_output, pretty_print=True, method="html"))

# print("Transformation complete! Output saved as output.html")
