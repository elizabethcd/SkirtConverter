# SkirtConverter

## Purpose

This script allows spritesheets of pants/skirts for Stardew Valley to be converted for use with the Fashion Sense (FS) framework (v4.11.2 and later). For more information on FS, see the [FS wiki](https://github.com/Floogen/FashionSense/wiki).

Feedback is welcome via Github issues or the Stardew Valley Discord (please include the exact error encountered and whether you're on Mac/Windows/Linux).

## Basic Instructions

1. Download Python and install it for your OS.
2. Install the packages used, if needed:
     1. In a Terminal (Mac or Linux) window, type `pip install pillow` and hit return. If you're in Windows, use Powershell and type ``py -m pip install pillow`` instead.
     2. Similarly, type `pip install argparse` (or `py -m pip install argparse`) and hit return.
     3. The other packages used should be default python packages.
3. Download the python script from Github (Green "Code" button, then "Download as .zip" option, then unzip).
4. Make a folder named `input` inside the source code file.
5. Place any .pngs inside the `input` folder, named with something that will become the final skirt/pants name. **PNGs must have the dimensions and layout of the vanilla skirt/pants items, meaning they are 192 by 688 pixels.**
6. Use `cd` to navigate into the folder with the python script and the json, or open a terminal window in that folder
    1. On a Mac, see the detailed guide for three different ways to do this.
    2. On Windows, open File Explorer to the folder you want, click on the address bar, type `powershell`, and hit return.
    3. If you use Linux you can check out info on `cd` for your distro (or see Mac guide)
7. Run the python script ``skirt_converter.py`` by typing ``python skirt_converter.py`` and hitting return. By default, the script pulls from the right side (female farmer base), but you can set a flag ``--rightHalf False`` to pull from the left side instead. By default, the script does not convert bathing suit sprites, but you can set a flag ``--bathingSuit True`` to include them. 
8. In the `output` folder, some folders will be generated. You can place these in a folder named `Pants` in an FS mod folder. 

If any of the initial Python installation steps or running the Python script are giving you trouble, you can reference the detailed guides from my furniture converter that also relies on Python:

Here's a detailed guide on how to use the furniture script, with screenshots, for Mac users: https://github.com/elizabethcd/FurnitureConverter/blob/main/docs/Mac_guide.md#mac-detailed-pictorial-install-guide

Here's a detailed guide on how to use the furniture script, with screenshots, for Windows users:
https://github.com/elizabethcd/FurnitureConverter/blob/main/docs/Windows_guide.md#windows-detailed-pictorial-install-guide

Here's a detailed guide on how to use the furniture script, with screenshots, for Linux users (thank you to Gerber for making it!):
https://github.com/elizabethcd/FurnitureConverter/blob/main/docs/Linux_guide.md#linux-detailed-pictorial-install-guide

## Known Issues

* Fashion Sense 4.11.2 or later is required. Using earlier versions will cause a fatal crash in specific circumstances. 
* Fashion Sense uses slightly the wrong sprites for clubs. This applies to both clubs and club special attacks. This will be fixed in a future FS version and the changes for this may need to be accomodated in this script depending on their implementation. 
* Fashion Sense does not allow for gendered clothing. If you want to create clothing matching both genders on the original spritesheet (left and right sides), run the script twice to make two clothing items. 

Fashion Sense bugs (not due to this script):
* Fashion Sense has a small bug with sitting from moving where it uses the wrong sprites.
* Slingshot arms are invisible when wearing anything FS. 

## Planned Updates

None so far, let me know if there's anything you're interested in seeing. Depending on how much sanity it sounds like it will cost, I may implement it.
