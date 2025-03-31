<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Student Details</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    table { border-collapse: collapse; width: 50%; }
                    th, td { border: 1px solid black; padding: 8px; text-align: left; }
                </style>
            </head>
            <body>
                <h2>Student Details</h2>
                <table>
                    <tr><th>Field</th><th>Value</th></tr>
                    <tr><td>Name</td><td><xsl:value-of select="student/name"/></td></tr>
                    <tr><td>Age</td><td><xsl:value-of select="student/age"/></td></tr>
                    <tr><td>Class</td><td><xsl:value-of select="student/class"/></td></tr>
                    <tr><td>Roll Number</td><td><xsl:value-of select="student/rollNumber"/></td></tr>
                    <tr><td>Email</td><td><xsl:value-of select="student/email"/></td></tr>
                    <tr><td>Address</td><td><xsl:value-of select="student/address"/></td></tr>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
