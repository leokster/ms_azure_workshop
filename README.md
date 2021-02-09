# Microsoft Azure Workshop

This repo helps to get startet with the microsoft Azure Portal and
more specifically with the virtual machines in it. The repo is 
splited in a manuals section and an example, which can be run as
a service an a Microsoft Azure virtual machine. 

### Manuals
- [How to create a virtual machine in Azure](manuals/creating_virtual_machine.md)
- [How to connect to a virtual machine](manuals/connect_to_vm.md)
- [How to setup Python on a VM](manuals/setup_anaconda_python.md)
- [How to to mount an Azure blob storage](manuals/mount_blob_storage.md)
- How to connect your IDE with the virtual Machine:
    - [PyCharm](manuals/setup_pycharm_ssh.md)
    - [VS Code](manuals/setup_vs_code_ssh.md)
- [How to work with Git](manuals/work_with_git.md) IN PROGRESS

### Example
As a small proof of concept project, we will setup a service an a
VM, which will send an email every day at 6 pm an email to you with
a random dinner recipe. Continue [here](examples/recipe_sender/README.md) for the manual. 


### Workshop 10.02.2021
We are going to do the following:
1. Setup SSH on your private Laptop (for [Windows](https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows), [Windows 10](https://www.antary.de/2020/02/01/ssh-keys-direkt-unter-windows-10-erstellen/), for mac and linux just type ``ssh-keygen`` in a terminal)
2. Add the SSH key to jetbrains space
3. setup the VM
4. Add ssh key of the VM to jetbrains space
5. Install conda
6. create an environment
7. clone git repo
8. Install the recipe sender
9. Test the recipe sender