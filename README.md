# twics_downloader
Automatic downloader in a range of weekly chess games, called twics from [theweekinchess](https://theweekinchess.com/twic). 

## Specs
* Supports downloads in any valid range of twics. eg:1352-1362. To find if a number is valid, check [theweekinchess](https://theweekinchess.com/twic) webpage.
* Downloads are made in zip files by default. In order to get the common chess file type pgn accepted by most chess programs, you will have to unzip manually each file.

## Running this code:

First of all download/clone the repository on your desired directory, then you have to install some dependencies if you dont have them:

```Batchfile
  pip install requests==2.27.1
```
After installing the required module,proceed with modifying the *config.json* file. 

This file has 3 items:
* initial_twic_2download: Number of the first twic to download.
* final_twic_2download: Number of the last twic to download.
* file_folder: Desired location (*path*) for the downloaded twics, the folder that will be used to store the twics must exist.

