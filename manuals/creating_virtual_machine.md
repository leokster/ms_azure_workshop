## Creating an Ubuntu VM in Azure
1. Go to the Azure portal
1. Click create a resource
1. Choose ``Ubuntu Server 18.04 LTS``
1. Choose a name for your VM
1. Choose a size for your VM. Attention if you choose a VM 
with no GPU you can't change it into one with GPU later. CPU
scaling is no problem later.
1. Check the box ``SSH public key``
1. Choose as username `ubuntu`
1. Select `Use existing public key` under SSH public key source
1. Paste your SSH public key into the text box. Checkout [this](https://www.ssh.com/ssh/keygen/) for
creating SSH keys
1. For basic and Disk there are no further modifications needed
1. Go to Networking 
1. Choose a Virtual Network (if you don't know what it is, it is probably
not relevant for you)
1. Click ``Create new`` for Public IP
1. Go to the next section (Management)
1. Check ``System assigned managed identity``
1. If you want check ``Enable auto-shutdown`` such that the VM
doesn't cause any costs during night e.g.
1. Click Create