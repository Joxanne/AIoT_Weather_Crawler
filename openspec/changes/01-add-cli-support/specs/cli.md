# Spec: CLI Support

## ADDED Requirements

### CLI-001: Database Path Argument
The system MUST accept a `--db` argument to specify the SQLite database file path.

#### Scenario: Default Database
Given the user runs the script without arguments
When the script executes
Then it should use `sqlitedata.db` as the default database

#### Scenario: Custom Database
Given the user runs `python weather_crawler.py --db my_weather.db`
When the script executes
Then it should use `my_weather.db` for storage

### CLI-002: Verbose Mode
The system MUST accept a `--verbose` or `-v` flag to enable detailed logging.

#### Scenario: Verbose Output
Given the user runs `python weather_crawler.py -v`
When the script fetches data
Then it should print detailed progress messages
