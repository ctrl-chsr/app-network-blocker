# Application Network Blocker

A Python script to block/unblock specific applications from accessing the internet using Windows Firewall rules.
For the original context, I need a workaround to block the network connection for my Steam game, because it requires an internet connection to launch the game.

## Features

- Block/unblock specific applications from accessing the internet
- Supports both inbound and outbound rules
- Works with any executable application

## Prerequisites

- Windows operating system
- Python 3.x
- Administrative privileges (required for modifying Windows Firewall rules)

## Usage

### Python Script

```bash
python block_app_internet.py [options] <path_to_executable>
```

Options:
- `-b` or `--block`: Block internet access for the specified application
- `-u` or `--unblock`: Unblock internet access for the specified application
- `-h` or `--help`: Show help message

Example:
```bash
# Block internet access for an application
python block_app_internet.py -b "C:\Program Files\MyApp\MyApp.exe"

# Unblock internet access for an application
python block_app_internet.py -u "C:\Program Files\MyApp\MyApp.exe"
```

### Batch File Usage

You can create batch (.bat) files to quickly block or unblock applications without typing the full command. Here's how:

1. Create a new text file with `.bat` extension
2. Add the Python command with desired options
3. Save and run as administrator

Example batch file (`block_steam.bat`):
```batch
@echo off
python block_app_internet.py -b "C:\Program Files (x86)\Steam\Steam.exe"
pause
```

Example batch file (`unblock_steam.bat`):
```batch
@echo off
python block_app_internet.py -u "C:\Program Files (x86)\Steam\Steam.exe"
pause
```

## Steam Usage Example

### Blocking Steam
To block Steam from accessing the internet:

1. Method 1 - Using Python script directly:
```bash
python block_app_internet.py -b "C:\Program Files (x86)\Steam\Steam.exe"
```

2. Method 2 - Using batch file:
- Create `block_steam.bat` with the content shown above
- Right-click and "Run as administrator"

### Unblocking Steam
To restore Steam's internet access:

1. Method 1 - Using Python script directly:
```bash
python block_app_internet.py -u "C:\Program Files (x86)\Steam\Steam.exe"
```

2. Method 2 - Using batch file:
- Create `unblock_steam.bat` with the content shown above
- Right-click and "Run as administrator"

## Important Notes

- Always run the script or batch files with administrative privileges
- The script creates Windows Firewall rules with names that include the application's filename
- Blocking an application affects both incoming and outgoing connections
- Make sure to use the correct path to the executable you want to block

## Troubleshooting

If you encounter any issues:
1. Ensure you're running as administrator
2. Verify the path to the executable is correct
3. Check Windows Firewall is enabled and running
4. Look for existing rules with the same name in Windows Firewall

## Next

[] Support linux and macOS operating system