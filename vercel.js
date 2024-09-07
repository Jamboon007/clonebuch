{
    "builds" = [{
        "src": "web_comsci/wsgi.py",
        "use": "@vercel/python"
    }],
    "routes" = [{
        "src": "/(.*)",
        "dest": "web_comsci/wsgi.py"
    }]
}