#!/usr/bin/env bash
echo "Password may be needed for installing pip: "
install_pip() {
	read -p "Would you like to install pip? (y/n): " install
	case $install in
		y)
			echo "Installing pip...\n"
			sudo apt install python3-pip
			;;
		n)
			echo "exiting..."
			;;
	esac
}
venv () {
	python -m venv ~.ven
}
