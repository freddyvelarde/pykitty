#!/usr/bin/bash

if ! git --version > /dev/null 2>&1; then
  echo "Git is not installed. Please install Git and try again."
  exit 1
fi

mkdir pykitty 
cd pykitty 

# Clone the repository
git init
git remote add origin  https://github.com/freddyvelarde/pykitty
git pull origin master

cd ../
mv ./pykitty ~/.config


if ! grep -q 'export PATH=$PATH:$HOME/.config/pykitty' ~/.zshrc; then
  sed -i '1i export PATH=$PATH:$HOME/.config/pykitty' ~/.zshrc
  source ~/.zshrc || true
else
  echo "pykitty already set it"
fi

echo "Pykitty was installed successfully"

