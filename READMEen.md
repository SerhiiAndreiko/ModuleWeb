# Personal Assistant

Project to create a "Personal Assistant" with a command-line interface.

Our "Personal Assistant" is a console bot that interacts with the user through a command-line interface, receiving commands and performing necessary actions.

The "Personal Assistant" is capable of:

- Storing contacts with names, addresses, phone numbers, emails, and birthdates in a contact book.
- Displaying a list of contacts whose birthdays are within a specified number of days from the current date.
- Validating the correctness of entered phone numbers and emails during contact creation or editing and notifying the user in case of incorrect input.
- Searching for contacts within the contact book.
- Editing and deleting entries from the contact book.
- Storing notes with textual information.
- Performing searches within notes.
- Editing and deleting notes.
- Adding "tags" to notes, which are keywords describing the topic or subject of the note.
- Searching and sorting notes by tags (keywords).
- The bot can analyze entered text and predict what the user wants from it, suggesting the nearest command for execution.
- Sorting files in a specified folder into categories (images, documents, videos, etc.).

## Note

The "Personal Assistant" sorts files in the specified folder into the following categories:

CATEGORIES = 
    "Audio": [".mp3", ".aiff", ".wav", ".aac", ".flac"]

    "Documents": [".docx", ".doc", ".txt", ".pdf", ".xls", ".xlsx", ".pptx", ".rtf"]

    "Video": [".avi", ".mp4", ".mov", ".mkv", ".mpeg"]

    "Image": [".jpeg", ".png", ".pcd", ".jpg", ".svg", ".tiff", ".raw", ".gif", ".bmp"]

    "Archive": [".zip", ".7-zip", ".7zip", ".rar", ".gz", ".tar"]

    "Book": [".fb2", ".mobi"]

All other files will be categorized as "Other".

## Usage

The application supports the following commands:

         hello  -> displays a welcome message.
         add -> adds a new contact.
         add birthday -> add a birthday to a contact.
         add note -> adds a new note.
         add tag -> adds a new tag to a note.
         edit birthday -> changes an existing contact's birthday.
         days to birthday -> shows how many days are left until a birthday.
         show birthday -> shows a list of contacts with birthdays within a specified number of days from the current date.
         edit phone -> changes an existing contact's phone number.
         del phone -> deletes a phone number from a contact.
         del note -> deletes a note.
         add phone -> adds a phone number to an existing contact.
         change phone -> replaces an old phone number with a new one.
         change note -> edits an existing note.
         show all -> displays all contacts and their phone numbers.
         show notes -> shows all notes.
         search by name -> searches for contacts with matching names.
         search by phone -> searches for contacts with matching phone numbers.
         search note by tag -> searches for a note with a specific tag.
         search note -> searches for a note within the text.
         sort folder -> sorts files by categories in the specified folder and deletes empty folders in the user-specified path.
         help -> displays a list of available commands.
         exit, close, good bye -> exits the program.

## Operation Features

The project is saved in a separate repository and publicly accessible at https://github.com/plaha303/Team10_Core_Progect.
The project includes detailed instructions for installation and usage.
The project is installed as a Python package and can be invoked from anywhere in the system after installation.
The Personal Assistant stores information on the hard drive in a user folder and can be restarted without data loss.

## Work Description

The AddressBook class inherits from UserDict and is responsible for the logic of searching for records in this class.
The Record class is responsible for adding/editing/removing optional fields and storing the mandatory Name field.

Record entries in AddressBook are stored as values in a dictionary, using Record.name.value as keys.
Record stores a Name object and a list of Phone objects in separate attributes.
Record implements methods for adding/removing/editing Phone objects.
AddressBook implements the add_record method, which adds a Record to self.data.

Pagination (page-wise output) is added to AddressBook for situations where the book is very large and needs to be displayed in parts rather than all at once. This is implemented through the creation of an iterator for records.

## Creating and Installing the "Personal Assistant"

To install the program, navigate to the directory containing the installation package and enter 'pip install Address-Book' in the command line (or python setup.py install, requiring administrator rights).

Once the package is installed in the system, the script can be invoked from anywhere using the command 'book' in the console.