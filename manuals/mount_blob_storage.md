## Create Connection from Azure VM to Blob Storage V2

You need for the following at least a virtual machine on 
Microsoft Azure and a Blob Storage V2 on Azure as well as at
least one container. We call the container `raw` in the following.
You can replace it by any other name. **Attention**: Make sure that
you check the box ``System assigned managed identity`` during creation
of the VM.

First of all go to your storage account in the Azure portal
and select the menu `Access Control (IAM)` and click `+ Add` and
then `Add role assignment`. Choose as role `Contributor`, as Assign access to
``Virtual Machine`` and then select your machine. 

Install Packages for Blob connection

```
wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb

sudo dpkg -i packages-microsoft-prod.deb

sudo apt-get update

sudo apt-get install blobfuse
```


Create folder in /mnt where the temporary files are stored (you won't access these folders directly later)

```
sudo mkdir /mnt/resource/blobfusetmp_raw -p
```

Set the rights of the corresponding folders

```
sudo chmod a+rwx /mnt/resource/blobfusetmp_raw/
```

Create a config file for the connection

```
sudo touch /etc/fuse_connection_raw.cfg
```

Add the following content to the files

```
accountName <your_storage_account_name>
authType MSI
containerName raw
```

make folder where you want to mount the dirves

```
sudo mkdir /media/raw
```

add a crontab (such that it automatically connects after reboot). Run

```
sudo crontab -e
```

and then add at the end of the file the following

```
@reboot sudo blobfuse /media/raw --tmp-path=/mnt/resource/blobfusetmp_raw  --config-file=/etc/fuse_connection_raw.cfg -o attr_timeout=240 -o entry_timeout=240 -o negative_timeout=120 -o allow_other
```