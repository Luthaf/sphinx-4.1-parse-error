import os

extensions = ["breathe"]

breathe_projects = {
    "code": os.path.join(os.path.dirname(__file__), "..", "xml"),
}

breathe_default_project = "code"
