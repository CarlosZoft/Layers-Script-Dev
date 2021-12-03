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