make sure to use MX linux live ISO
## Partition Disks
```
cfdisk $DISK
```
## make File-systems

```
mkfs.fat -F 32 $BOOTPART
mkswap $SWAPPART
mkfs.btrfs  $ROOTPART
```
## create Sub-volumes

```
mount $ROOTPART
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@opt
btrfs subvolume create /mnt/@var
btrfs subvolume create /mnt/@tmp
btrfs subvolume create /mnt/@nix
umount $ROOTPART
```

## Mount Filesystems

```
mount -o rw,ssd,space_cache,noatime,compress=zstd,commit=120,subvol=@ $ROOTPART /mnt
mkdir /mnt/{home,boot,opt,var,tmp}
mount -o rw,ssd,space_cache,noatime,compress=zstd,commit=120,subvol=@home $ROOTPART /mnt/home
mount -o rw,ssd,space_cache,noatime,compress=zstd,commit=120,subvol=@opt $ROOTPART /mnt/opt
mount -o rw,ssd,space_cache,noatime,compress=zstd,commit=120,subvol=@var $ROOTPART /mnt/var
mount -o rw,ssd,space_cache,noatime,compress=zstd,commit=120,subvol=@tmp $ROOTPART /mnt/tmp
mount -o rw,ssd,space_cache,noatime,compress=zstd,commit=120,subvol=@nix $ROOTPART /mnt/nix
mount $BOOTPART /mnt/boot
```

## Debootstrap

- make sure to include some important programs 
```
debootstrap \
  --exclude nano \
  --include locales,grub2,linux-image-amd64,sudo,vim,btrfs-progs,arch-install-scripts,efibootmgr,network-manager,git,build-essential,man,linux-firmware \
  --arch=amd64
  bullseye
  /mnt
```
## Write `fstab`



## Install Grub
```
grub-install --target=x86_64-efi --efi-directory=/mnt/boot --root-directory=/mnt --bootloader-id=Mint $DISK
```
## Mount /dev /dev/pts /sys /proc
things
## Chroot into installation and begin Configuration

- set keyboard options
- install grub-btrfs
- picom
- xinit


## Update Grub

- unmount things from last step
- use arch-chroot
- make sure to install linux image beforehand
## `Chroot ` into installation

- set locales, tzdata, set time
- install additional programs
  - btrfs-progs, efibootmgr, neovim git build-essential, linux-image, timeshift, grub-btrfs
  - desktop enviroment, window manager
## Create User
## Edit `Sudo` Permission
## Install Necessary Programs
list of programs

- xfce4-panel
- neofetch
- xfce4-terminal
- lxappearance
- gnome-keyring
- picom
- firefox
- brave
- steam
- alacritty
- "display manager"
- correct fonts
