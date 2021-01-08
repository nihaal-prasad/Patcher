#!/usr/bin/env python3
import keystone
import argparse

# Parse the arguments
parser = argparse.ArgumentParser(description="Patches data inside of binary executables in Linux.")
parser.add_argument("file", help="Executable to modify.", nargs="?")
parser.add_argument("addr", help="The address of the data/instruction to modify (written in hex).", nargs="?")
parser.add_argument("data", nargs="*", help="The data to write at addr (written in space-separated hex or assembly).")
parser.add_argument("-a", "--assembly", action="store_const", const=True, default=False, help="Data is code that must be assembled before being written.")
parser.add_argument("--arch", nargs="?", default="x86_64", help="Architecture to use if -a is specified (default is x86_64).")
parser.add_argument("--list-architectures", action="store_const", const=True, default=False, help="List all supported architectures.")
args = parser.parse_args()

# List supported architectures if necessary
if(args.list_architectures):
    print("""Supported Architectures:
- arm
- arm64
- mips
- mips64
- ppc
- ppc64
- sparc
- sparc64
- x86
- x86_64""")
    exit()

# Figure out the architecture
arch = None
mode = None
if(args.arch == "arm"):
    arch = keystone.KS_ARCH_ARM
    mode = keystone.KS_MODE_ARM
elif(args.arch == "arm64"):
    arch = keystone.KS_ARCH_ARM64
    mode = keystone.KS_MODE_ARM
elif(args.arch == "mips"):
    arch = keystone.KS_ARCH_MIPS
    mode = keystone.KS_MODE_MIPS32
elif(args.arch == "mips64"):
    arch = keystone.KS_ARCH_MIPS
    mode = keystone.KS_MODE_MIPS64
elif(args.arch == "ppc"):
    arch = keystone.KS_ARCH_PPC
    mode = keystone.KS_MODE_PPC32
elif(args.arch == "ppc64"):
    arch = keystone.KS_ARCH_PPC
    mode = keystone.KS_MODE_PPC64
elif(args.arch == "sparc"):
    arch = keystone.KS_ARCH_SPARC
    mode = keystone.KS_MODE_SPARC32
elif(args.arch == "sparc64"):
    arch = keystone.KS_ARCH_SPARC
    mode = keystone.KS_MODE_SPARC64
elif(args.arch == "x86"):
    arch = keystone.KS_ARCH_X86
    mode = keystone.KS_MODE_32
elif(args.arch == "x86_64"):
    arch = keystone.KS_ARCH_X86
    mode = keystone.KS_MODE_64
else:
    print("Invalid architecture.")

# Convert the address into an integer
addr = int(args.addr, 16)

# Initialize data variable
data = None

# Assemble data if necessary
if(args.assembly):
    # Convert data from a list into a space-separate string
    data = ""
    for thing in args.data:
        data += thing + " "
    ks = keystone.Ks(arch, mode)
    data, count = ks.asm(data, addr)
else:
    # Else, convert data into an array of hex bytes
    data = []
    for x in range(0, len(args.data)):
        data.append(int(args.data[x], 16))

# Patch the binary
with open(args.file, "rb+") as f:
    f.seek(addr)
    f.write(bytearray(data))
