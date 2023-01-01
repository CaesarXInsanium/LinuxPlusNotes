#! /bin/env python3
import subprocess as sub
import shutil
import os
from os import geteuid


TARGET_DIR = "/mnt"
SUBVOLUMES = [
    "home",
    "opt",
    "var",
    "tmp",
    "nix",
    "gnu"
]
SUBVOL_OPTIONS = [
    "noatime",
    "compress=zstd",
    "ssd"
]
RELEASE = "bookworm"
PACKAGES = (
    "arch-install-scripts",
    "cryptsetup",
    "cryptsetup-initramfs",
    "zstd",
    "vim",
    "grub2",
    "grub-efi-amd64",
    "dosfstools",
    "btrfs-progs",
    "efibootmgr",
    "linux-image-amd64",
    "sudo",
)


def is_root():
    return geteuid() == 0


def partition():
    print("Starting Installation")

    print("Enter Drive to Install")
    sub.run(["df", "-l"])
    drive = input("Enter Drive> ")
    print("Manually make 4 Partitions")
    sub.run(["fdisk", drive])
    efi_part = f"{drive}1"
    boot_part = f"{drive}2"
    swap_part = f"{drive}3"
    root_part = f"{drive}4"
    sub.run(["mkfs.fat", "-F", "32", efi_part])
    sub.run(["mkfs.ext4", boot_part])
    sub.run(["mkswap", swap_part])
    print("Encrypting Root Partition")
    sub.run(["cryptsetup", "luksFormat", root_part])
    luks = input("Name Crypt Volume >")
    sub.run(["cryptsetup", "luksOpen", root_part, luks])
    luks = f"/dev/mapper/{luks}"
    sub.run(["mount", luks, TARGET_DIR])

    sub.run(["btrs", "su", "cr", f"{TARGET_DIR}/@"])
    for vol in SUBVOLUMES:
        sub.run(["btrfs", "su", "cr", f"{TARGET_DIR}/@{vol}"])

    sub.run(["umount", TARGET_DIR])
    sub.run(["mount", "-o", ])
    for vol in SUBVOLUMES:
        opts = ",".join(SUBVOL_OPTIONS)
        sub.run(["mkdir", f"{TARGET_DIR}/{vol}"])
        sub.run(
            ["mount", "-o", f"{opts},subvol=@{vol}", luks, f"{TARGET_DIR}/{vol}"])

    sub.run(["mkdir", f"{TARGET_DIR}/boot"])
    sub.run(["mount", boot_part, f"{TARGET_DIR}/boot"])

    sub.run(["mkdir", f"{TARGET_DIR}/boot/efi"])
    sub.run(["mount", efi_part, f"{TARGET_DIR}/boot/efi"])
    sub.run(["swapon", swap_part])
    sub.run(["lsblk"])


if is_root():
    partition()
else:
    print("Missing Root Privelages")
