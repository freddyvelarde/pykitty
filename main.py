from src.config.paths import vim_dir, kitty_dir
from src.file_handler import switcher
from src.argparse import args, parser
from src.config.colorschemes import kitty_colorschemes, vim_colorschemes


def main():
    if not args.vim and not args.kitty and not args.all:
        return parser.error("what you want to do? please pass --vim or --kitty")


    if args.vim:
        if args.vim_theme in vim_colorschemes:
            switcher(vim_dir, vim_colorschemes[args.vim_theme])
            print("nvim theme was changed")
        else:
            print(f'theme: {args.vim_theme} not found')

    if args.kitty:
        if args.kitty_theme in kitty_colorschemes:
            switcher(kitty_dir, kitty_colorschemes[args.kitty_theme])
            print("kitty terminal theme was changed")
        else:
            print(f'theme: {args.kitty_theme} not found')

    if args.all:
        if not args.theme in kitty_colorschemes:
            return print(f'theme: {args.theme} not found in your kitty themes')

        if not args.theme in vim_colorschemes:
            return print(f'theme: {args.theme} not found in your nvim themes')

        switcher(kitty_dir, kitty_colorschemes[args.theme])
        switcher(vim_dir, vim_colorschemes[args.theme])
        print("kitty terminal and nvim themes was changed")
