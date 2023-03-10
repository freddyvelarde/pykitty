# Pykitty

This script is inspired in [ pycritty ](https://github.com/antoniosarosi/pycritty/)

if you're interested in this script and automating your nvim or/and kitty color scheme
you can install this CLI.

## DISCLAIMER!!!

> This python script only works with my folder structure
> both with nvim and with kitty terminal,
> if you want to use it you will need to take my nvim and kitty config
> or edit the script (it is not complicated)

**Table of Contents**

- [:wrench: Requirements](#requirements)
- [:wrench: Installation](#installation)
- [:gem: Usage](#usage)

<a id="requirements"></a>

# :wrench: Requirements

To use this CLI program you need to have installed git and python3

<a id="installation"></a>

# :wrench: Installation

```shell
curl https://raw.githubusercontent.com/freddyvelarde/pykitty/master/install.sh | bash
```

<a id="usage"></a>

# :gem: Usage

when you use --all argument, this will change the colorscheme in kitty and nvim at
the same time.

```shell
pykitty --all --theme tokyo
```

Unlike "--all" --vim only will switch the nvim colorscheme

```shell
pykitty --vim --vim-theme tokyo
```

# GALLERY:

Nightfly colorscheme
![kitty nightfly](./screenshots/nightfly-kitty.png)
![nvim nightfly](./screenshots/nightfly-nvim.png)

Decay colorscheme
![kitty decay](./screenshots/decay-kitty.png)
![nvim decay](./screenshots/decay-nvim.png)

Rose-pine colorscheme
![kitty rosepine](./screenshots/rosepine-kitty.png)
![nvim rosepine](./screenshots/rosepine-nvim.png)

Gotham colorscheme
![kitty gotham](./screenshots/gotham-kitty.png)
![nvim gotham](./screenshots/gotham-nvim.png)

Onedark colorscheme
![kitty Onedark](./screenshots/onedark-kitty.png)
![nvim Onedark](./screenshots/onedark-nvim.png)

Tokyo colorscheme
![kitty tokyo](./screenshots/tokyo-kitty.png)
![nvim tokyo](./screenshots/tokyo-nvim.png)
