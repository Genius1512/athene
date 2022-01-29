# Athene

Developed by Silvan Schmidt \
[MIT License](license)

## Requirements

- [Python 3.10](https://www.python.org/downloads/release/python-3100/ "Python 3.10 Install link")
- [Pip](https://www.liquidweb.com/kb/install-pip-windows/ "Tutorial to download pip")
- [PIP Requirements](requirements.txt "Requirements")

## Features

### Data

#### API

Run ```athene data api <ip> <port>``` to launch an API with all data available. \
Open your browser at ```<ip>:<port>/data/<identifier>``` to recveive the data you want.
![API Data](assets\imgs\api_data.png "Example of a data set")

#### Get

Run ```athene data get <identifier>``` to get the data of \<identifier\>

#### Search

Run ```athene data search <search term>``` to search profiles containing the \<search term\>

### Timetable

Run ```athene tt <class name>``` to get the timetable of the class \<class name\>. \
Does not show cancelled lessons!

### Beamer

Still in development, does not work

### Get Menu

Run ```athene menu``` to get todays menu in the canteen

## Download files from site

Powershell:
```powershell
Invoke-WebRequest -Uri <url> -OutFile <outfile>
```
