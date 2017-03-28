# How to install:
## Creating NSRL Database:
1. Create a folder for the DB to reside in and change in to the folder just created

```
mdkir ~/NSRL-DB
cd ~/NSRL-DB
```
3. Download the NSRL data base from https://www.nsrl.nist.gov/Downloads.htm I prefer to use the minimal set

```
wget https://www.nsrl.nist.gov/RDS/rds_2.55/rds_255_modernm.zip
```
4. If not already installed, install unzip and extract the NSRLFile.txt from the ZIP file amd rename it to .csv

```
sudo apt-get install unzip
unzip rds_255_modernm.zip NSRLFile.txt
mv NSRLFile.txt NSRLFile.csv
```
6. If not already installed, install sqlite3 and convert the .csv file to a database

```
sudo apt-get install sqlite3
sqlite3 NSRL.db
.mode csv
.import NSRLFile.csv nsrl
```

## Getting Docker ready:
Issue the following docker-compose command to build the image:

```
docker-compose build
```

# How to use:
## Starting up docker:
To start this API as a service isse the following command:

```
docker-compose up -d
```

## Making HTTP Post to the service:
Here is a sample POST to the API:

```
curl -X POST -F "hash=0000002D9D62AEBE1E0E9DB6C4C4C7C16A163D2C" "http://[IP_Address]:8080/api/v1/nsrl/query"
```
## API Responses:
The response received from the API is made up of 3 elements:
1. **response_code**:
    * 0 - *Lookup succeeded*; hash was found and date was returned
    * 1 - *Lookup succeeded*; NO matching hash could be found
    * 2 - *Input error*; the hash vallue provided could not be validated
    * 3 - *There was a database problem*;
2. **message**; a brief description of what didn't work
3. **info**; more details on what exactly was the problem or caused the issue

# How to create a NSEL db file:
1. Download the latest veriosn of the NSRL (https://www.nsrl.nist.gov/Downloads.htm) I pefere to use the minimal set
2. Extract the file "NSRLFile.txt" to a location of your choice
3. Renmae the file to "NSRLFile.csv"
4. Open the command-line and run the following commands
 * (You will need the appropriate binary to edit & view sqlite files: https://sqlite.org/download.html):

```
sqlite3.exe nsrl.db
.mode csv
.import NSRLfile.csv nsrl
```
The last command will take time to complete depending on the hardware you are using for this task.

This will result in a file being created in the folder where you ran the command sqlite3 commands from called nsrl.db. This database will conain one table called nsrl which contains all the data that was contained in the NSRLFile.txt that was downloaded.
Lastly in order to free up some space on the disk it is recommended to delete the original file downloaded from the NSRL website as well as the extracted file.
