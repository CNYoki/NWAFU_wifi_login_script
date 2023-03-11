all:
	buildBinary

confVenv:
	@echo "Configureing venv ..."
	python3 -m venv buildEnv
	@echo "You need to activate the venv manually by running 'source ./buildEnv/bin/activate'"

buildBinary:
	@echo "Installing dependencies ..."
	@pip3 install -r requirements.txt
	@echo "Building binary ..."
	@pyinstaller --onefile --noconfirm --log-level=DEBUG --name=nwafuLogin loginScript.py
	@echo "Remember to deactivate the venv by running 'deactivate'"
	@echo "You can now run the binary by running './dist/nwafuLogin'"
	@echo "You can also install the systemd unit file and timer by running 'make install'"
	@echo "Remember to change your username and password in the systemd/nwafuLogin.service file before installing the systemd unit file and timer"

install:
	@echo "Installing systemd unit file and timer..."
	cp systemd/nwafuLogin.service /etc/systemd/system/
	cp systemd/nwafuLogin.timer /etc/systemd/system/
	@echo "Reloading systemd daemon ..."
	@systemctl daemon-reload
	@echo "Enabling timer ..."
	@systemctl enable nwafuLogin.timer
	@echo "Starting timer ..."
	@systemctl start nwafuLogin.timer
	@echo "Installing binary ..."
	cp dist/nwafuLogin /usr/bin/
	@echo "Done!"

clean:
	@echo "Cleaning ..."
	@rm -rf buildEnv
	@rm -rf build
	@rm -rf dist
	@rm -rf __pycache__
	@rm -rf *.spec

