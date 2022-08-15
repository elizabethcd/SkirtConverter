# SkirtConverter

Work in progress

1. Download Python and install it for your OS
2. Download the source code and unzip it
3. Make a folder named `input` inside the source code file
4. Place any .pngs inside the `input` folder, named with something that will become the final skirt/pants name. PNGs must have the dimensions and layout of the vanilla skirt/pants items, meaning they are 192 by 688 pixels. 
5. Run the python script ``skirt_converter.py``. By default, the script pulls from the right side (female farmer base), but you can set a flag ``--rightHalf False`` to pull from the left side instead. By default, the script does not convert bathing suit sprites, but you can set a flag ``--bathingSuit True`` to include them. 
6. In the `output` folder, some folders will be generated. You can place these in a folder named `Pants` in an FS mod folder. You may need to do some small tweaks.

If any of the initial steps are giving you trouble, you can reference the detailed guides from my furniture converter that also relies on Python:

Here's a detailed guide on how to use the furniture script, with screenshots, for Mac users: https://github.com/elizabethcd/FurnitureConverter/blob/main/docs/Mac_guide.md#mac-detailed-pictorial-install-guide

Here's a detailed guide on how to use the furniture script, with screenshots, for Windows users:
https://github.com/elizabethcd/FurnitureConverter/blob/main/docs/Windows_guide.md#windows-detailed-pictorial-install-guide

Here's a detailed guide on how to use the furniture script, with screenshots, for Linux users (thank you to Gerber for making it!):
https://github.com/elizabethcd/FurnitureConverter/blob/main/docs/Linux_guide.md#linux-detailed-pictorial-install-guide
