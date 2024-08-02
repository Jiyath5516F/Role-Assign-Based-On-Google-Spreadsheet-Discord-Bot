# Role Assign Based On Google Spreadsheet Discord Bot

## Purpose of this bot:
This app automatically assign roles for users on discord based on **Based On Google Spreadsheet** response.

## Note:
⚠️⚠️ USE THIS ON YOUR OWN RISK ⚠️⚠️!!

#### Step 1: Create a Google Cloud Project
1. Go to the Google Cloud Console : Google Cloud Console
2. Create a New Project:
    - Click on the project dropdown (top left) and select "**New Project**."
    - Give your project a name and click "**Create**."
#### Step 2: Enable Google Sheets and Google Drive APIs
1. Select Your Project: Make sure your new project is selected.
2. Enable APIs:
    - In the left sidebar, navigate to `APIs & Services > Library`.
    - Search for Google Sheets API and click on it.
    - Click Enable.
    - Do the same for Google Drive API.
#### Step 3: Create Service Account Credentials
1. Go to Credentials:
In the left sidebar, navigate to APIs & Services > Credentials.
2. Create Credentials:
    - Click on Create Credentials and select Service Account.
    - Fill in the details and click Create.
3. Grant Permissions (if needed): You can skip this step for now.
4. Create Key:
    - After creating the service account, click on it to open its details.
    - Go to the Keys tab and click on `Add Key > JSON`. This will download a JSON file to your computer.
#### Step 4: Share Your Google Sheet with the Service Account
1. Open Your Google Sheet: Go to the Google Sheet you want to use.
2. Share the Sheet:
    - Click on the Share button in the top right corner.
    - Enter the service account email (found in the JSON file) and give it Editor access.
Click Send.
#### Step 5: Install Required Python Packages
Open your terminal and install the required packages:
```bash
pip install gspread oauth2client discord.py
```
or

```bash
pip install -r requirements.txt
```

#### Step 6: Run Your Bot
Make sure you have your Google Sheet and Discord bot properly set up. Run your Python script:

```bash
python app.py
```

For any help: [https://discord.com/users/831836517516312586](https://discord.com/users/831836517516312586)
