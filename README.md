# ground_truth_GUI

This project is a tool I developed in order to get ground truth feedback from a huge set of scanned hand written documents.
The tool was implemented to register which type of seal, if any, the documents had printed on as well as their respectives
coordinates in the image. A prototype for the selected seal is displayed as well. The utility also lets you register and save the
images to a folder on the fly of new seal types that might get discovered while iterating through the document images.

The script opens two windows. One of them uses pygame to display the document image, move it and zoom it in and out with the mouse
wheel. It also lets you select the seal position by marking the corners of its bounding rectangle using mouse buttons (one button
for each corner.

The other window has been coded using tkinter. It allows the user to select the apropiate seal, store new seals found and send the
data to the database.

For this code to work, a mySQL database properly setup is needed. A set of images is needed as well. The last requirement is a txt
file called index.txt that is used as an index pointing to the next image to be cataloged.

The MAIN SCRIPT TO RUN is pygame_tkinter_integration.py.

More detailed instructions on the database setup as well as the file structure coming soon.


Known bugs:
  1) Storing a new seal prototype does not make it appear in the seal list (restarting required).
  2) Storing a new seal from a document won't automatically catalog the given document, its necesary to do it again.
