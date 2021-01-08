# Patcher
This is a small Python script that allows you to easily modify binary files.

### Usage
```
usage: patcher.py [-h] [-a] [--arch [ARCH]] [--list-architectures] [file] [addr] [data]

Patches data inside of binary executables in Linux.

positional arguments:
  file                  Executable to modify.
  addr                  The address of the data/instruction to modify (written in hex).
  data                  The data to write at addr (written in space-separated hex or assembly).

optional arguments:
  -h, --help            show this help message and exit
  -a, --assembly        Data is code that must be assembled before being written.
  --arch [ARCH]         Architecture to use if -a is specified (default is x86_64).
  --list-architectures  List all supported architectures.
```
