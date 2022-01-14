most_util_tags = {
    "docker": "-d",
    "nvm and yarn": "-n -y",
}

data = [
    {
        "directory": "tendaedu-backend",
        "flag": most_util_tags['docker'],
        "type": "Docker",
    },
    {
        "directory": "layers-auth-vanilla",
        "flag": most_util_tags['nvm and yarn'],
        "type": "Auth Interface",
    },
    {
        "directory": "tendaedu-backend",
        "flag": most_util_tags['nvm and yarn'],
        "type": "Backend",
    }
]
docker = {
   "layers-comunicados": {
       "docker": {
        "directory": "layers-comunicados",
        "flag": most_util_tags['docker'],
       }
    },
    "layers-payments": {
        "docker": {
        "directory": "payments",
        "flag": most_util_tags['docker'],
        }    
    },
}
apps = {
    "layers-comunicados": {
        "interface" : {
            "directory": "layers-comunicados/web",
            "flag": most_util_tags['nvm and yarn'],
        },
        "backend": {
            "directory": "layers-comunicados/app",
            "flag": most_util_tags['nvm and yarn'],
        }
    },
    "layers-design-system": {
        "interface" : {
            "directory": "layers-design-system",
            "flag": most_util_tags['nvm and yarn'],
        }
    },
    "layers-payments": {
        "interface" : {
            "directory": "payments/app",
            "flag": most_util_tags['nvm and yarn'],
        }
    },
    "layers-webapp": {
        "interface" : {
            "directory": "layers-webapp",
            "flag": most_util_tags['nvm and yarn'],
        }
    },
    "tendaedu-backend": {
        "interface" : {
            "directory": "tendaedu-backend/web",
            "flag": most_util_tags['nvm and yarn'],
        },
        "backend": {
            "directory": "tendaedu-backend/app",
            "flag": most_util_tags['nvm and yarn'],
        }
    }
}