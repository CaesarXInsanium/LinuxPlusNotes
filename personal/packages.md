# Packages

## Important for Installation

- arch-install-scripts
- cryptsetup
- cryptsetup-initramfs 
- zstd
- vim
- grub2
- grub-efi-amd64
- dosfstools
- btrfs-progs
- efibootmgr
- linux-image-amd64
- sudo

## Important for Usefulness

- network-manager
- htop

## Command

```sh
useradd -m -s /bin/bash -g sudo $USER
dpkg-reconfigure tzdata
dpkg-reconfigure locales
cryptsetup luksFormat --type luks1
```

## Initramfs

```text
Using /etc/initramfs-tools/conf.d/cryptsetup is deprecated in stretch.

The new preferred method is to set "CRYPTSETUP=y" in /etc/cryptsetup-initramfs/conf-hook.
```
