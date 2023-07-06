# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:50:10 2023

@author: monster
"""
import os
import base64
from github import Github
from pprint import pprint

username = "x4nth055"
access_token = "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"

# Create a PyGithub object with your access token
g = Github(access_token)
# get that user by username
user = g.get_user(username)
# make a directory to save the Python files
if not os.path.exists("python-files"):
    os.mkdir("python-files")

def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    try:
        for content in repo.get_contents(""):
            # check if it's a Python file
            if content.path.endswith(".py"):
                # save the file
                filename = os.path.join("python-files", f"{repo.full_name.replace('/', '-')}-{content.path}")
                with open(filename, "wb") as f:
                    f.write(content.decoded_content)
            print(content)
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except Exception as e:
        print("Error:", e)
        # search repositories by name
for repo in g.search_repositories("pythoncode tutorials"):
    # print repository details
    print_repo(repo)