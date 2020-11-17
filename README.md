# Tagging Fixer

This script fixes issues in tagged data that result in an erroneous shifting of <ae> tags.

## Error
The error occurs in the 'ae' step in the tagging process. It occurs when a single document contains more than one <ae> tag, and after processing, all documents that contain <ae> tags are shifted. The shifting doesn't begin, however, until after the first document with two tags.
    
In order to prevent this error from occurring, this script should be run at any time after the initial 'entry' step and before 'ae'. Afterwards, continue tagging the data as before.

## How it works
The script simply combines the <ae> tags that lie within a single document. These are then stored in a new <ae> tag and separated with '###'

The script also outputs the document IDs of all effected documents, allowing for manual checking of the data.

The affected tags should be checked in the final data to confirm that no errors arose as a result of the combining of the tags. This also allows for the opportunity to remove the '###' from the data and any other errors that may occur.

### Common resulting error
A common error that appears is the following:

    <ae_ex>305 - 311, août 1753 et XII, 206-215, nov. ### Autres éditions:</ae_ex>
    
Normally, the text "Autres éditions:" is separated into an <ae_ae> tag, however this only works with the first time this text appears.

In order to properly separate the data, either remove everything after the '###', or create a new tag as follows:

    <ae_ex>305 - 311, août 1753 et XII, 206-215, nov.</ae_ex>
    <ae>Autres éditions:<ae>
    
Other similar errors may appear. How to fix these issues is at the discretion of the user.

## Usage

To execute the script, Python 3 and pip3 are required.

In order to run the script, either download the ZIP version of this repository and unpack it or clone it using the following:

    git clone https://github.com/AaronWinziers/TaggingFixer.git
    
Before executing, the location of the files that need to be checked should be amended in line 4 of the script.
    
Navigate into the folder containing the code, and execute the following in order to install the required packages:

    pip3 install -r requirements.txt

Then, enter the following to execute the script:

    python3 main.py
    
