# SBMP Filetype

Here I have created the **.sbmp** file extension.
It stands for `Scratch Bitmap Image File`, but only the `Scratch Bitmap` part is in the extension.

## Viewing .sbmp files

To get started, download the repository. Make sure you have python and pip installed.

Next, install the dependencies.
`pip install -r requirements.txt`

Then, on Windows, set up the viewer.py to view .sbmp files. This can be done by:

Start Menu -> Default Programs -> Type '.sbmp' and click `Choose a default` -> Navigate to the downloaded repo -> Choose sbmpViewer.bat

Now, double-clicking any .sbmp file will open with the viewer.py file.

## Converting .sbmp files

Converting files is quite easy. In the directory of the repository, open a terminal window.

Type `python converter.py <filename.jpg/png> <size [preferably something like 240 or 360]> <output filename .sbmp>`
