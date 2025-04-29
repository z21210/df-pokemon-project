import pandas as pd
import pytest
from src.main import load_pokemon

@pytest.fixture
def cleaned_data():
    """Fixture for data after loading and cleaning"""
    return load_pokemon()

def test_load_pokemon_drops_friendship_column(cleaned_data):
    assert (
        "base_friendship" not in cleaned_data.columns
    ), "base_friendship column should be dropped"
    
def test_load_pokemon_drops_experience_column(cleaned_data):
    assert (
        "base_experience" not in cleaned_data.columns
    ), "base_experience column should be dropped"