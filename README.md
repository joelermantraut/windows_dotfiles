# Windows Dotfiles

This repository contains my own Windows OS dotfiles. Also, I
wrote a little guide to important post-installation configs.

# Steps
1. Install [Alacritty Terminal Emulator](https://github.com/alacritty/alacritty).
2. In Alacritty properties (From Windows Menu) change "Start on" property to where you want it to start.
3. Do the same with all CMDs (CMD, Powershell, etc.).
4. Install [JetBrains Mono Font](https://github.com/JetBrains/JetBrainsMono).
5. Install [Git](https://gitforwindows.org/).
6. Install [Station](https://stationhq.com/).
7. Install [Keypirinha + Everything](https://keypirinha.com/install.html).
8. Install [XtremeeDownloadManager](https://xtremedownloadmanager.com/).
9. Install [Python](https://www.python.org/downloads/).
10. Install [Pip](https://bootstrap.pypa.io/get-pip.py).
11. Install [Choco Package Manager](https://chocolatey.org/install).
12. Install [Gopass](https://www.gopass.pw/).
13. Install [GPG](https://www.phildev.net/pgp/gpginstall).
14. Copy GPG Key, and downloads or copy passwords folder.
15. [Config Gopass to use already copied password folder](https://github.com/gopasspw/gopass/blob/master/docs/setup.md#new-password-store-with-git).
  - Copy GPG Key.
  - Clone password repository.
  - >gopass init
  - >gopass config path "password_folder_path"
16. [Install SSH client](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

# After that
This repository files are config files of differente programs. It depends where you installed it,
but mostly, you can use the same directory like here to copy them.