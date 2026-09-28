#!/usr/bin/env python3
"""Exercise real skills CLI install/update/remove in disposable projects."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from skill_catalog import discover

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--cli-path', help='Existing skills 1.7.0 bin/cli.mjs')
args = parser.parse_args()
cli = ['node', args.cli_path] if args.cli_path else [shutil.which('npx') or 'npx', '--yes', 'skills@1.7.0']
env = dict(os.environ, DO_NOT_TRACK='1', DISABLE_TELEMETRY='1', NO_COLOR='1')
def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, env=env, text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(result.stdout)
    return result.stdout

skills = discover()
with tempfile.TemporaryDirectory(prefix='buspro-install-') as tmp:
    root = Path(tmp)
    source = root / 'source'
    source.mkdir()
    for skill in skills.values():
        shutil.copytree(skill.path, source / 'skills' / skill.name)
    run(['git', 'init', '-b', 'main'], source)
    def commit():
        run(['git', 'add', '.'], source)
        run(['git', '-c', 'user.name=Packaging Test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture'], source)
    commit()
    projects = []
    for mode in ('copy', 'symlink'):
        project = root / mode
        project.mkdir()
        command = cli + ['add', source.as_uri(), '--skill', *skills, '--agent', 'codex', 'claude-code', 'antigravity', 'cline', '--yes']
        if mode == 'copy':
            command += ['--copy']
        run(command, project)
        projects.append(project)
        for name, skill in skills.items():
            for host in ('.agents', '.claude'):
                installed = project / host / 'skills' / name
                assert (installed / 'SKILL.md').read_bytes() == (skill.path / 'SKILL.md').read_bytes(), installed
    # Move package locations and change content, then prove reinstall refreshes both. Generic file URLs cannot exercise the hosted updater.
    for skill in skills.values():
        target = source / 'skills' / skill.category / skill.name
        target.parent.mkdir(exist_ok=True)
        shutil.move(str(source / 'skills' / skill.name), target)
        with (target / 'SKILL.md').open('a', encoding='utf-8') as stream:
            stream.write('\nPackaging update marker.\n')
    commit()
    for project in projects:
        output = run(cli + ['add', source.as_uri(), '--skill', *skills, '--agent', 'codex', 'claude-code', 'antigravity', 'cline', '--yes'], project)
        for name in skills:
            for host in ('.agents', '.claude'):
                assert 'Packaging update marker.' in (project / host / 'skills' / name / 'SKILL.md').read_text(encoding="utf-8"), output
        run(cli + ['remove', *skills, '--yes'], project)
        for name in skills:
            for host in ('.agents', '.claude'):
                assert not (project / host / 'skills' / name).exists()
print('PASS: copy/symlink installation, category-move reinstall, and removal for all three skills across four host targets.')
