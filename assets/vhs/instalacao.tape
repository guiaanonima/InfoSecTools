# Where should we write the GIF?
Output instalacao.gif

# style layout
Set WindowBar Colorful
Set Theme "Dracula"
Set Margin 20
Set MarginFill "#0554f1"
Set BorderRadius 10

# Set up a 1200x600 terminal with 32px font.
Set FontSize 22
Set Width 1200
Set Height 600

# Login as Root
Type "su"
Sleep 1400ms
Enter

# Type a password
Type "casaos"
Enter
Sleep 1400ms
Hide
Type "clear"
Enter
Show

# Cloning Repo
Type "git clone https://github.com/guiaanonima/InfoSecTools.git"
Sleep 1200ms
Enter
Sleep 2100ms
Hide
Type "clear"
Enter
Show

# Access Folder
Type "cd InfoSecTools"
Sleep 1000ms
Enter
Sleep 700ms
Hide
Type "clear"
Enter
Show

# Install Requeriments
Type "pip install -r requirements.txt"
Sleep 2000ms
Enter
Sleep 4000ms
Hide
Type "clear"
Enter
Show

# Admire the output for a bit.
Sleep 2s