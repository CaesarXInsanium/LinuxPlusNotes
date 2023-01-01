#! /bin/bash

echo "Installing Debian"
RELEASE=bookworm
PACKAGES= arch-install-scripts \
    cryptsetup \
    cryptsetup-initramfs \
    zstd \
    vim \
    grub2 \
    grub-efi-amd64 \
    dosfstools \
    btrfs-progs \
    efibootmgr \
    linux-image-amd64 \
    sudo


# Partition Drive
echo "Enter Drive to Install"
lsblk
## Create EFI, BOOT, SWAP ROOT Partition
## encrypt ROOT Partition
## create subvolumes
## mount subvolumes

# Debootstrap
## mount Packages

# Create User
# Configure Locales, Time zone
# Create User and Configure sudo privalages
# enable services

# Generate Fstab
# write crypttab
# configure initramfs
# configure GRUB

# 
