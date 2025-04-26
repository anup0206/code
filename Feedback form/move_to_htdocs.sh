```bash
   #!/bin/bash

   # Source directory (where your files are located)
   SRC_DIR="$HOME/projects/form"

   # Destination directory (XAMPP htdocs)
   DEST_DIR="/opt/lampp/htdocs"

   # Files to move
   FILES=("index.html" "submit.php")

   # Check if source directory exists
   if [ ! -d "$SRC_DIR" ]; then
       echo "Error: Source directory $SRC_DIR does not exist."
       exit 1
   fi¬

   # Check if destination directory exists
   if [ ! -d "$DEST_DIR" ]; then
       echo "Error: Destination directory $DEST_DIR does not exist."
       exit 1
   fi

   # Loop through files and copy them
   for FILE in "${FILES[@]}"; do
       if [ -f "$SRC_DIR/$FILE" ]; then
           echo "Copying $FILE to $DEST_DIR..."
           sudo cp "$SRC_DIR/$FILE" "$DEST_DIR/$FILE"
           if [ $? -eq 0 ]; then
               echo "Successfully copied $FILE."
           else
               echo "Error: Failed to copy $FILE."
               exit 1
           fi
       else
           echo "Error: $FILE not found in $SRC_DIR."
           exit 1
       fi
   done

   # Set permissions for files in htdocs
   echo "Setting permissions for files in $DEST_DIR..."
   sudo chmod 644 "$DEST_DIR/index.html" "$DEST_DIR/submit.php"
   if [ $? -eq 0 ]; then
       echo "Permissions set successfully."
   else
       echo "Error: Failed to set permissions."
       exit 1
   fi

   echo "All files moved successfully to $DEST_DIR!"
   echo "You can access the form at http://localhost/index.html"
   ```