"""
Unit tests for receiver.py
"""
import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from config import Config, DevelopmentConfig, ProductionConfig, TestConfig


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
        """Test testing configuration"""
        config = TestConfig()
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
    """Basic tests for receiver functionality"""
   
    def test_receiver_imports(self):
        """Test that receiver.py can be imported"""
        try:
            # This will test if the file has valid Python syntax
            import receiver
            assert True
        except ImportError:
            # If taipy or other dependencies aren't installed, that's okay for now
            pytest.skip("Receiver dependencies not installed")
        except SyntaxError:
            pytest.fail("receiver.py has syntax errors")
   
    def test_config_integration(self):
        """Test that config can be used in receiver"""
        from config import current_config
        assert current_config is not None
        assert hasattr(current_config, 'PORT')
        assert hasattr(current_config, 'HOST')