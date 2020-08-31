#Creure 
import os

sublimeText = ["wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -", 'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list', "sudo apt-get update", "sudo apt-get install sublime-text"]
protonVPN = ["sudo apt install -y openvpn dialog python3-pip python3-setuptools", "sudo pip3 install protonvpn-cli" ]
python3Pip = ["sudo apt-get install python3-pip", "sudo pip3 install protonvpn-cli"]


for command in sublimeText:
	print(os.system(command))

for command in protonVPN:
	print(os.system(command))

