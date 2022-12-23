#!/usr/bin/bash
if ! grep -q 'export PATH=$PATH:$HOME/dev/projects/CLI/theme-switcher' ~/.zshrc; then
  sed -i '1i export PATH=$PATH:$HOME/dev/projects/CLI/theme-switcher' ~/.zshrc 
  source ~/.zshrc || true
# echo "Word not found in file.txt"
else 
  echo "pykitty already set it"
fi

