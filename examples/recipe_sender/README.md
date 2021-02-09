# Recipe Sender

This script sends you a random recipe from gutekueche.de by email. 
Follow these steps to make it work. 

1. Clone the repo to your VM
    ```
   git clone ssh://git@git.jetbrains.space/swissgrid/microsoft-azure-workshop/ms_azure_workshop.git
    ```
1. Navigate to the recipe-project folder 
    ```
    cd ./ms_azure_workshop/examples/recipe_sender/
    ```
1. Activate your python environment (if you don't know what this is, just
skip this step)
    ```
   conda activate <your-python-env>
    ```
1. Install dependencies
    ```
    pip install -r requirements.txt
    ```
1. Create a file `email_credentials.yml` 
    ```
   touch email_credentials.yml
    ```
1. Edit the file by running ``nano email_credentials.yml`` and type in the following
    ```
    user: <email-address>
    pw: <email-password>
    server: <smtp-server>
    ```
1. Modify the recipients.txt file and add for every recipient one email address
per line.
    ```
    nano recipients.txt
    ```
1. Run the script.
    ```
   python run.py    
    ```
1. If you want you can add the job to the crontab by running (check [this](https://crontab.guru)).
    ```
    crontab -e
    ```
   