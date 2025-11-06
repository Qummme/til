import nox

@nox.session(venv_backend="none")
def check(session):
    session.run("uv", "run", "scripts/check_tags.py", "--active", external=True)

@nox.session(venv_backend="none")
def index(session):
    session.run("uv", "run", "scripts/build_tag_index.py", "--active", external=True)

