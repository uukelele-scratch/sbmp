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

You can then double-click them to view (if you have done the previous steps)

## Viewing in Scratch

The entire purpose of .sbmp files is for them to be able to be viewed on Scratch. So, here's the link to the .sbmp viewer.

https://scratch.mit.edu/projects/1107520357/

Inside the project, show the .sbmp upload list, right-click it and click `import`. Then, change to `all files` in File Explorer, and select the output.sbmp file from your folder. Finally, run the project with a green flag or click the custom block. This will render the sbmp file to your screen.

## What's the point?

You may have realised Scratch already offers this functionality, to be able to add images to your project. That's why this has a reason: ScratchAttach Cloud Requests.

ScratchAttach (by @TimMcCool) has a feature named Cloud Requests that allow data to be transferred between the Scratch project and a python backend. This means that we can use it to transfer the .sbmp file, after converting it, through the project and rendering it.
