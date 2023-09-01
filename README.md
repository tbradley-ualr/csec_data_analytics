# Setup

## PyCharm Project Setup

1. **Environment Setup**
   
   Open the project folder in PyCharm. It should prompt you to set up a virtual environment using Python 3.11 and 
2. synchronize with the `requirements.txt` file present in the project root.

   Alternatively, you can manually set up the environment by executing the following commands:

   ```commandline
   python -m venv venv
   python -m pip install -r requirements.txt
   ```
   To activate virtual envronment: `source venv/bin/activate`
   To deactivate venv: `venv`

2. **Enable Django Support**

   - Navigate to `File` -> `Settings` -> `Languages and Frameworks` -> `Django`. <br>
     (On Mac: Navigate to `PyCharm` -> `Preferences` -> `Languages and Frameworks` -> `Django`.)
   - Check the box to enable Django support.
   - Set the Django Project Root to this project folder's root.
   - For the settings, choose `csec_data_analytics/settings.py`.
   - Make sure the manage script points to `manage.py` located at the project root.
     ![image](https://github.com/Emmaka9/csec_data_analytics/assets/28539986/993b7874-d954-4f67-8faf-92979124bee9)


3. **Django Run Configuration**

   - Go to `Run` -> `Edit Configurations`.
   - Click the plus (+) sign to add a new configuration, then select `Django server`.
   - Retain the default values and confirm with `OK`.

4. **Running the Django Server**

   Press the **Play** (▶️) or **Debug** button in the top right-hand corner. The terminal should display that the 
   server is running on port 8000.

5. **Creating and Running Management Commands**

   - To create a new management command, add a Python file under `csec_data_analytics_app/management/commands`. Name the file according to the command you intend.
   - Refer to the template in `csec_data_analytics_app/management/commands/my_command.py`.
   
   To execute your command:
   1. Go to `Tools` -> `Run manage.py Task`. This opens a terminal where you can input your command along with any 
      desired parameters.
   2. Alternatively, adjust your Django server run configuration. In the configuration settings, click on 
   3. `Run custom command`. Enter your command, ensuring you remove port 8000 and add any relevant parameters, 
   4. especially if debugging is needed.

## MongoDB Configuration

1. **Initialize Database and User**

   Start MongoDB Shell by running:

   ```commandline
   mongosh
   ```

   Then, execute the following commands:

   ```commandline
   // Create a new collection
   db.createCollection("django-mongo")

   // Switch to the new collection
   use django-mongo;

   // Create a user for the collection
   db.createUser({
       user: "admin",
       pwd: "put5gwz2bjx9phe!TUD",
       roles: [
           { role: "readWrite", db: "django-mongo" },
           { role: "read", db: "django-mongo" }
       ]
   })
   ```
