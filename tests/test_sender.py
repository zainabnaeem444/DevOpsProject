"""
Unit tests for sender.py
"""
import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from config import Config


class TestSenderConfig:
    """Test sender-specific configuration"""
   
    def test_sender_interval(self):
        """Test sender interval configuration"""
        config = Config()
        assert config.SENDER_INTERVAL >= 0
        assert isinstance(config.SENDER_INTERVAL, int)
   
    def test_sender_host_port(self):
        """Test sender host and port configuration"""
        config = Config()
        assert config.SENDER_HOST is not None
        assert config.SENDER_PORT > 0
        assert config.SENDER_PORT < 65536
   
    def test_pollution_ranges(self):
        """Test pollution data generation ranges"""
        config = Config()
        assert config.POLLUTION_MIN >= 0
        assert config.POLLUTION_MAX > config.POLLUTION_MIN
        assert config.NUM_SENSORS > 0


class TestSenderBasics:
    """Basic tests for sender functionality"""
   
    def test_sender_imports(self):
        """Test that sender.py can be imported"""
        try:
            import sender
            assert True
        except ImportError:
            pytest.skip("Sender dependencies not installed")
        except SyntaxError:
            pytest.fail("sender.py has syntax errors")
   
    def test_receiver_url_format(self):
        """Test that receiver URL is properly formatted"""
        from config import current_config
        assert current_config.RECEIVER_URL.startswith("http://")
        assert ":" in current_config.RECEIVER_URL