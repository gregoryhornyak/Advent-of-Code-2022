# Git Cheat Sheet

## Create repository

1. Create the directory on PC
2. ```git init```
3. ```git remote add <remote_name> <remote_repo_url>``` 
> use HTTP instead of HTTPS


## Clone repository

```git clone <repo_url>```
>already configured for remote collaboration

## Save updates

1. ```git add FILENAME```
2. ```git commit -m "message"```
3. ```git status```

## Declare author of commits

```git config --global user.name <name>```
or for local author name:
```git config --local user.name <name>```