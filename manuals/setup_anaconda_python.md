## Installing Anaconda and setting up virtual environment

```
sudo apt-get update
```

```
sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
```

```
bash Anaconda3-2020.11-Linux-x86_64.sh
```

Attention: logout and login to the VM to load ``conda`` into the path. 
```
exit
ssh ubuntu@<ip-address>
```

### Make Environment

Create a new environment
```
conda create --name py38 python=3.8
```

activate the envirionment
```
conda activate py38
```