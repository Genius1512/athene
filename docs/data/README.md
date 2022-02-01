<link rel="stylesheet" href="/athene/static/styles/standard.css">
<link rel="shortcut icon" type="image/x-icon" href="/athene/favicon.ico">

# Athene data

## Get

Get a users profile:
```bash
python athene data get <identifier>
```

Output:
```
<identifier>'s profile:
    Name: <name>
    Id: <id>
    ...
```

## Search

Search for a profile containing the given search term:
```bash
python athene data search <term>
```

## Data Searcher

You can also use the online tool: [Data Searcher](/athene/datasearcher) \
Enter a search term, if it is a perfect match, it'll show you the profile, otherwise it will \
show profiles that contain your search term

## API

Launch an API containing all known data:
```bash
python athene data api <ip, default "127.0.0.1"> <port, default 8000>
```

Then, go to  \<ip\>:\<port\>/data/\<identifier\>, to receive a profile as JSON-data
![Data](api_data.png "Data Example")
