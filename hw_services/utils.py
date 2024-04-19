"""
A Collection of useful functions for Python
"""

from __future__ import annotations

import subprocess
import sys
from typing import List, Optional


def run_cmd(
    cmd: List[str],
    *,
    check_results: bool = True,
    print_cmd: bool = False,
    print_output: bool = False,
    chomp: bool = False,
    cwd: Optional[str] = None,
) -> subprocess.CompletedProcess[str]:
    """Run a command with subprocess and catch any CalledProcessErrors."""
    if print_cmd:
        print(f"Running: {' '.join(cmd)}")
    try:
        process_results = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=check_results,
            cwd=cwd,
        )
        if print_output:
            print(process_results.stdout)
        if chomp:
            process_results.stdout = process_results.stdout.rstrip("\r\n\t ")
        return process_results
    except subprocess.CalledProcessError as err:
        print(f"CalledProcessError returned {err.returncode}")
        print(f"command: {err.cmd}")
        print(f"stdout: {err.stdout}")
        print(f"stderr: {err.stderr}")
        sys.exit(err.returncode)
