# OSM Scraping
Basic scripts for scraping player datas from Online Soccer Manager

## How To Install?
Only pip dependency is the Selenium package. It can be installed by:
```
pip install selenium
```
or 
```
pip install -r requirements.txt
```
Other dependency is the ChromeDriver. It can be downloaded from https://chromedriver.chromium.org/downloads. </br>
This project is developped using [version 91.0.4472.19](https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19/) </br> </br>
Download the file and copy it into the project's directory. <b>Do not rename the file.</b> If you are on Linux or OS X, change <i>chromedriver.exe</i> to <i>chromedriver</i> in both scripts.
</br>
After setting up the environment, run the Login script. If a chrome window is opened and you can view the OSM's webpage, you have set up your environment correctly </br>
## How To Use?
Run the Login script. Navigate to the login page. Enter your credentials. I suggest using a burner account. OSM's servers can block the account because of exceeded number of requests. <br/> <br/>
When login is completed and your account is accesible, close the window, and wait for the script to terminate. The login cookies are saved as a pickle file. </br>
Navigate to the project directory. If there is a file called <i>cookie.pkl</i> you may run the main script. </br>

## Download the Available Database
Database file can be found in [Releases](https://github.com/atuncer/OSM_Scraping/releases). </br>
Check the last updated date before downloading.
