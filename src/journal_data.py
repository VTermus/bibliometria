"""
This module provides loading utilities for the built-in datasets with journal data
"""

import pandas as pd
import importlib.resources
import os

# for efficiency: cache for loaded datasets 
_sjr_data = None
_wos_data = None


def _load_csv(filename):
    """ Load CSV file from package data """
    # modern approach for Python 3.9+
    try:
        with importlib.resources.files("journal_metrics.data").joinpath(filename).open() as f:
            return pd.read_csv(f)
    except (AttributeError, FileNotFoundError):
        # fallback for older Python
        try:
            with importlib.resources.open_text("journal_metrics.data", filename) as f:
                return pd.read_csv(f)
        except (FileNotFoundError, ModuleNotFoundError):
            # development fallback
            data_path = os.path.join(os.path.dirname(__file__), 'data', filename)
            return pd.read_csv(data_path)


def get_sjr():
    """ Get SJR 2024 data (cached) """
    global _sjr_data
    if _sjr_data is None:
        _sjr_data = _load_csv('sjr_journals_2024.csv')
    return _sjr_data


def get_wos():
    """ Get WOS data (cached) """
    global _wos_data
    if _wos_data is None:
        _wos_data = _load_csv('wos_journals.csv')
    return _wos_data





