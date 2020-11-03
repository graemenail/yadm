"""Test dump"""

import pytest


@pytest.mark.parametrize(
    'exists, executable, code, expect', [
        (False, False, 1, 'Cannot execute dump'),
        (True, False, 1, 'is not an executable program'),
        (True, True, 123, 'Dump successful'),
    ], ids=[
        'missing',
        'not executable',
        'executable',
    ])
def test_dump(
        runner, yadm_y, paths, exists, executable, code, expect):
    """Test dump command"""
    if exists:
        paths.dump.write('')
    if executable:
        paths.dump.write(
            '#!/bin/bash\n'
            f'echo {expect}\n'
            f'exit {code}\n'
        )
        paths.dump.chmod(0o775)
    run = runner(command=yadm_y('dump'))
    assert run.code == code
    assert run.err == ''
    assert expect in run.out
