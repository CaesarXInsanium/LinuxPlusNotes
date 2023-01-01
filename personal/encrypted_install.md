# Encrypted Install

## Steps

- install arch-installa scripts debootstrao
- created partitions
- luksforms root
- luksDump root
- create subvolumes
- mount subvolumes
- install base system
  - packages: efibootmgr, grub-efi-amd64, linux-image-amd64, cryptsetup, network-manager,
- set root password
- create user
- save UUID to /mnt/etc/crypttab
  - `LUKS UUID=<UUID> none luks`
- set grub kernel parameters

```text
GRUB_CMDLINE_LINUX_DEFAULT="quiet cryptdevice=/dev/vda3:LUKS root:/dev/mapper/LUKS"
GRUB_ENABLE_CRYPTODISK=y
```

- install grub
- update grub
 - `update-initramfs -u` check for no errors

1. Partition
2. Wipe Devices
3. LUKS
4. Btrfs Subvolumes
5. Install Base System
6. User Configuration
7. Services
8. Grub

## Partition

```bash
fdisk /dev/vda
```

- make suitable Partitions

## Wipe Devices

```bash
shred /dev/vda1 /dev/vda2
```
