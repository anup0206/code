<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <body>
            <h2>People</h2>
            <ul>
                <xsl:for-each select="root/person">
                    <li>
                        <xsl:value-of select="name"/> is <xsl:value-of select="age"/> years old.
                    </li>
                </xsl:for-each>
            </ul>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
