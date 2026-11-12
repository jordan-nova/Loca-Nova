## Full Documentation & Instructions:
## Read [PROJECT_BRIEF.md](./docs/PROJECT_BRIEF.md) for details regarding the project architecture and goals.

## ![Loca Nova Interface Preview](./preview.png)



# Loca Nova – Initial Project

## Description
This is the initial Python starter project for Loca Nova.

## Requirements
- Python 3
- No additional Python packages required for the current version.

## Configuration
Create a `.env` file in the project folder and add:

```env
APP_KEY=YOUR_OWN_TEST_KEY
```

Do not upload the real `.env` file to GitHub.

## Run
Start the application with:

```bash
python main.py
```

The local server runs at:

```text
http://127.0.0.1:8080/
```



## Test Commands
The server accepts POST requests at `/command`.

Supported commands:
- ON
- OFF

The current version validates commands but does not control real hardware.

## Project Status
This is an initial prototype for further development by the Loca Nova developer.
## Test Commands
The server accepts POST requests in JSON format at `/command`.

Example request body:
```json
{
  "password": "YOUR_OWN_TEST_KEY",
  "command": "ON"
}
```

Supported commands:
- ON
- OFF
