#!/usr/bin/env python3

import os
import json
import requests
from datetime import datetime
import hashlib

# Canva API endpoints
CANVA_API_BASE = "https://api.canva.com"
DESIGN_ENDPOINT = f"{CANVA_API_BASE}/v1/designs/{os.environ['CANVA_DESIGN_ID']}"
TOKEN_ENDPOINT = f"{CANVA_API_BASE}/oauth/token"

def get_access_token():
    """Get OAuth access token from Canva"""
    client_id = os.environ['CANVA_CLIENT_ID']
    client_secret = os.environ['CANVA_CLIENT_SECRET']
    
    response = requests.post(
        TOKEN_ENDPOINT,
        data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': 'design:read'
        }
    )
    
    if response.status_code != 200:
        raise Exception(f"Failed to get access token: {response.text}")
    
    return response.json()['access_token']

def get_current_cv_hash():
    """Get the hash of the current CV link in about.md"""
    with open('content/about.md', 'r') as f:
        content = f.read()
        # Extract the current CV link
        start = content.find('https://www.canva.com/design/')
        if start == -1:
            return None
        end = content.find('"', start)
        if end == -1:
            return None
        current_link = content[start:end]
        return hashlib.md5(current_link.encode()).hexdigest()

def get_design_version():
    """Get the current version of the design from Canva API"""
    try:
        access_token = get_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        response = requests.get(DESIGN_ENDPOINT, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to get design: {response.text}")
        
        design_data = response.json()
        # The version is typically in the metadata or last_modified field
        return design_data.get('version') or design_data.get('last_modified')
        
    except Exception as e:
        print(f"Error getting design version: {e}")
        return None

def check_cv_updates():
    """Check if the CV has been updated"""
    try:
        current_hash = get_current_cv_hash()
        if current_hash is None:
            print("Could not find current CV link")
            return False
            
        # Get the current version from Canva
        current_version = get_design_version()
        if current_version is None:
            print("Could not get current design version")
            return False
            
        # Store the version in a file to compare with next time
        version_file = '.github/cv_version.txt'
        try:
            with open(version_file, 'r') as f:
                last_version = f.read().strip()
        except FileNotFoundError:
            last_version = None
            
        # If versions are different, update the stored version
        if last_version != current_version:
            with open(version_file, 'w') as f:
                f.write(current_version)
            return True
            
        return False
        
    except Exception as e:
        print(f"Error checking CV updates: {e}")
        return False

if __name__ == "__main__":
    has_updates = check_cv_updates()
    # Set the output for GitHub Actions
    print(f"::set-output name=changed::{str(has_updates).lower()}") 