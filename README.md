# Discord Role Scraper

1. Clone repo
2. Start the scraper using `start.bat`
3. Input token
4. Input server ID
5. Enjoy scraping

> Your token is temporarily stored in memory for in-script caching. Your token is only ever sent to Discord.

[![Example Scraper Output](https://i.postimg.cc/Z5mr4bCf/Screenshot-75.jpg)](https://postimg.cc/56PHmM5v)

## Config

The `config.py` file allows you to choose what to scrape as well as if you want to export the scrape to a text file.

- `EXPORT_RESULTS (bool)`
    - Whether or not to export scrapes to a text file (saved as ./export/serverid_timestamp_roles.txt)

- `SCRAPE_GUILD_INFO (bool)`
    - Whether or not to scrape general guild info (e.g. owner ID, description, region, etc.)

- `GUILD_INFO_TO_SCRAPE (list[bool])`
    - What server atributes (excluding roles) to scrape
        - True = value is displayed
        - False = value is not displayed

- `SCRAPE_PERMISSION_INFO (bool)`
    - Whether or not to scrape roles and permissions

- `PERMISSIONS_TO_SCRAPE (dict[bool | int])`
    - What role attributes and permissions to scrape.
    - Keys with boolean values are non-permission attributes and can be toggled by changing their value
        - True = value is displayed
        - False = value is not displayed
    - Keys with non-boolean values are permission attributes and can __**NOT**__ be  toggled by changing their value
        - Comment or uncomment the line of each permission to show/not show
        - Values can't be changed because they are used in permission calculations (whether a role has a specific permission or not)
