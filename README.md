
This is a simple python script that allows you to increase the size of executable files by adding random or null bytes. This can be useful for various purposes, such as testing, bypassing file size checks.

## Features
- Increase file size by a specified number of KB.
- Option to append either random bytes or null bytes.
- Displays the final file size after modification.

## How It Works
1. The user provides the file name and the number of kilobytes to add.
2. The script opens the file, seeks to the end, and appends the chosen type of bytes.
3. Once the process is complete, the new file size is displayed.

## Usage
```py
[#] Enter FileName: myfile.exe
[#] Enter How Much KB You Need: 100
[?] Random Bytes Or Null Bytes? (R/N) N For Null
```
