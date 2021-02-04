## Setup Visual Studio Code for working with a VM

Similar to PyCharm it is also possible with VS Code to connect to
a virtual machine. The idea is slightly different since you connect
to the VM and then everything is done on the host. In comparison to PyCharm, where the setup is in a way, that the project folder is local and then mirrored to the host. There are advantages and disadvantages of both setups. The PyCharm Setup is probably easier for less experienced users, since you don't need to use any Git (mirroring is done automatically). It is also possible to setup a file sync with VS Code (see [this](https://code.visualstudio.com/docs/remote/ssh) for a full documentation). To sumarize: in PyCharm code is stored in general locally and is then copied to a `temp` folder on the host to execute. In VS Code you work in principle only on the host. There is no code or data from your local machine which is used directly on the host. 

### How to setup
1. Click File -> New File
2. Open the command plate (F1 on your keyboard)
3. Write `Extensions: Install Extensions`
4. In the Extensions Tab type in `Remote - SSH` and install it
5. Open again the command plate (F1)
6. type `Remote-SSH` and choose `Remote-SSH: add new SSH Host...`
7. Enter your credentials like `ssh ubuntu@<ip-address>`
8. open again the command plate (F1)
9. type `Remote-SSH` and choose `Remote-SSH: Connect to Host...`
10. Now there should open a new window where you see on the bottom line in green the IP address of your host machine, which indicates, that the connection worked. 