import os
home_dir = os.environ["HOME"]

# these are the file where will be overswrited
vim_dir = os.path.join(
    home_dir, ".config/nvim/lua/config/set-colorscheme.lua")

kitty_dir = os.path.join(
    home_dir, ".config/kitty/set-colorscheme.conf")
