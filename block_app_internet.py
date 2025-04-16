#!/usr/bin/env python3
import os
import sys
import ctypes
import argparse
import subprocess
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def block_app(app_path, app_name=None):
    """Block internet access for the specified application."""
    app_path = Path(app_path)
    
    if not app_path.exists():
        print(f"Error: {app_path} not found.")
        print("Please verify the application path and try again.")
        return False
    
    if app_name is None:
        app_name = app_path.stem
    
    try:
        # Block outbound traffic
        subprocess.run([
            "netsh", "advfirewall", "firewall", "add", "rule",
            f"name=Block {app_name} Outbound",
            "dir=out",
            "action=block",
            f"program={app_path}",
            "enable=yes"
        ], check=True)
        
        # Block inbound traffic
        subprocess.run([
            "netsh", "advfirewall", "firewall", "add", "rule",
            f"name=Block {app_name} Inbound",
            "dir=in",
            "action=block",
            f"program={app_path}",
            "enable=yes"
        ], check=True)
        
        print(f"\nInternet access has been blocked for {app_name}.")
        print(f"To unblock, run: python {sys.argv[0]} --unblock --name \"{app_name}\"")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating firewall rules: {e}")
        return False

def unblock_app(app_name):
    """Unblock internet access for the specified application."""
    try:
        # Remove outbound rule
        subprocess.run([
            "netsh", "advfirewall", "firewall", "delete", "rule",
            f"name=Block {app_name} Outbound"
        ], check=True)
        
        # Remove inbound rule
        subprocess.run([
            "netsh", "advfirewall", "firewall", "delete", "rule",
            f"name=Block {app_name} Inbound"
        ], check=True)
        
        print(f"\nInternet access has been restored for {app_name}.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error removing firewall rules: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Block or unblock internet access for applications")
    parser.add_argument("--unblock", action="store_true", help="Unblock internet access")
    parser.add_argument("--path", help="Path to the application executable")
    parser.add_argument("--name", help="Name of the application (optional)")
    
    args = parser.parse_args()
    
    # Ensure we have admin privileges
    run_as_admin()
    
    if args.unblock:
        if not args.name:
            print("Error: Application name is required for unblocking")
            print("Usage: python block_app_internet.py --unblock --name \"Application Name\"")
            return
        unblock_app(args.name)
    else:
        if not args.path:
            print("Error: Application path is required for blocking")
            print("Usage: python block_app_internet.py --path \"path_to_application.exe\" [--name \"Application Name\"]")
            return
        block_app(args.path, args.name)

if __name__ == "__main__":
    main() 