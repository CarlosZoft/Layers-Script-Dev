most_util_tags = {
    "docker": "-d",
    "nvm and yarn": "-n -y",
}

data = [
    {
        "directory": "tendaedu-backend",
        "flag": most_util_tags['docker'],
    },
    {
        "directory": "layers-webapp",
        "flag": most_util_tags['nvm and yarn'],
    },
    {
        "directory": "layers-auth-vanilla",
        "flag": most_util_tags['nvm and yarn'],
    },
    # {
    #     "directory": "tendaedu-web/app",
    #     "flag": most_util_tags['nvm and yarn'],
    # },
    # {
    #     "directory": "tendaedu-web/web",
    #     "flag": most_util_tags['nvm and yarn'],
    # },
    {
        "directory": "tendaedu-backend",
        "flag": most_util_tags['nvm and yarn'],
    }
]

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
    }
}