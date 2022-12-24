import argparse


parser = argparse.ArgumentParser()


parser.add_argument("-v", "--vim", action="store_true",
                    help="use --vim if you want to switch your nvim colorscheme")
parser.add_argument("-vt", "--vim-theme", help="change only vim colorscheme")


parser.add_argument("-k", "--kitty", action="store_true",
                    help="use --kitty if you want to switch your kitty terminal colorscheme")
parser.add_argument("-kt", "--kitty-theme",
                    help="change only kitty colorscheme")

parser.add_argument("-a", "--all", action="store_true", help="change nvim and kitty themes")
parser.add_argument("-t", "--theme", help="change global colorscheme")



args = parser.parse_args()
