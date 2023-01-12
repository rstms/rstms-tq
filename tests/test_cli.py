# cli tests

from subprocess import run


def test_run():
    proc = run(["tq", ".", "pyproject.toml"])
    assert proc.returncode == 0, proc
