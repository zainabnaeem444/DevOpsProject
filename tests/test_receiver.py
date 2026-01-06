"""
Unit tests for receiver.py
"""
import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from config import Config, DevelopmentConfig, ProductionConfig
from config import TestConfig as AppTestConfig


class TestConfig:
    """Test configuration management"""
   
    def test_default_config(self):
        """Test default configuration values"""
        config = Config()
        assert config.APP_NAME == "EcoMetrics"
        assert config.VERSION == "1.0.0"
        assert config.PORT == 5000
        assert config.HOST == "0.0.0.0"
   
    def test_development_config(self):
        """Test development configuration"""
        config = DevelopmentConfig()
        assert config.DEBUG == True
        assert config.LOG_LEVEL == "DEBUG"
   
    def test_production_config(self):
        """Test production configuration"""
        config = ProductionConfig()
        assert config.DEBUG == False
        assert config.LOG_LEVEL == "WARNING"
        assert config.RECEIVER_HOST == "receiver-service"
   
    def test_test_config(self):
        config = AppTestConfig()  # ← Use renamed import
        assert config.DEBUG == True
        assert config.SENDER_INTERVAL == 0
   
    def test_config_display(self, capsys):
        """Test config display method"""
        config = Config()
        config.display_config()
        captured = capsys.readouterr()
        assert "EcoMetrics Configuration" in captured.out
        assert "Version:" in captured.out


   
class TestReceiverBasics:
    def test_receiver_file_exists(self):
        """Test that receiver.py exists"""
        import os
        assert os.path.exists("src/receiver.py")
    
    def test_receiver_syntax(self):
        """Test receiver.py has valid Python syntax"""
        import py_compile
        py_compile.compile("src/receiver.py", doraise=True)
   
    def test_config_integration(self):
        """Test that config can be used in receiver"""
        from config import current_config
        assert current_config is not None
        assert hasattr(current_config, 'PORT')
        assert hasattr(current_config, 'HOST')