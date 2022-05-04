#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

from __future__ import annotations

import os
from pathlib import Path

__all__ = [
    "datasets_dir",
    "pretrained_dir",
]


# MARK: - Directories

__current_file  = os.path.abspath(__file__)                    # "workspaces/one/projects/aic/src/aic/utils.py"
source_root_dir = os.path.dirname(__current_file)              # "workspaces/one/projects/aic/src/aic"
pretrained_dir  = os.path.join(source_root_dir, "pretrained")  # "workspaces/one/projects/aic/src/aic/pretrained"

datasets_dir   = os.getenv("DATASETS_DIR", None)  # In case we have set value in os.environ
if datasets_dir is None:  # Run in debug mode from PyCharm
    datasets_dir = os.path.join(str(Path(source_root_dir).parents[2]), "datasets")  # "workspaces/one/datasets
if not os.path.isdir(datasets_dir):
    print(datasets_dir)
    # raise RuntimeWarning("`datasets_dir` has not been set.")
