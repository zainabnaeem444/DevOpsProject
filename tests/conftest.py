"""
Pytest configuration and fixtures
"""
import pytest
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


@pytest.fixture
def sample_config():
    """Fixture to provide a sample configuration"""
    from config import Config
    return Config()


@pytest.fixture
def dev_config():
    """Fixture to provide development configuration"""
    from config import DevelopmentConfig
    return DevelopmentConfig()


@pytest.fixture
def prod_config():
    """Fixture to provide production configuration"""
    from config import ProductionConfig
    return ProductionConfig()