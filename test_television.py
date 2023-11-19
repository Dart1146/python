import pytest
from television import Television


class TestTelevision:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2

    def test_init(self):
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'
        assert str(self.tv2) == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.power()
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'

        self.tv2.power()
        assert str(self.tv2) == 'Power = True, Channel = 0, Volume = 0'

        self.tv2.power()
        assert str(self.tv2) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.mute()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.power()
        self.tv1.mute()
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 1'

        self.tv1.power()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 1'

        self.tv2.power()
        self.tv2.volume_up()
        self.tv2.mute()
        assert str(self.tv2) == 'Power = True, Channel = 0, Volume = 0'

        self.tv2.mute()
        assert str(self.tv2) == 'Power = True, Channel = 0, Volume = 1'

        self.tv2.power()
        self.tv2.mute()
        assert str(self.tv2) == 'Power = False, Channel = 0, Volume = 1'

        self.tv2.power()
        assert str(self.tv2) == 'Power = True, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tv1.channel_up()
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_up()
        assert str(self.tv1) == 'Power = True, Channel = 1, Volume = 0'

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert str(self.tv1) == 'Power = True, Channel = 0, Volume = 0'

        self.tv2.channel_up()
        assert str(self.tv2) == 'Power = False, Channel = 0, Volume = 0'

        self.tv2.power()
        self.tv2.channel_up()
        assert str(self.tv2) == 'Power = True, Channel = 1, Volume = 0'

        self.tv2.channel_up()
        self.tv2.channel_up()
        self.tv2.channel_up()
        assert str(self.tv2) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.channel_down()
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_down()
        assert str(self.tv1) == 'Power = True, Channel = 3, Volume = 0'

        self.tv1.channel_down()
        assert str(self.tv1) == 'Power = True, Channel = 2, Volume = 0'

        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        assert str(self.tv1) == 'Power = True, Channel = 3, Volume = 0'

        self.tv2.channel_down()
        assert str(self.tv2) == 'Power = False, Channel = 0, Volume = 0'

        self.tv2.power()
        self.tv2.channel_down()
        assert str(self.tv2) == 'Power = True, Channel = 3, Volume = 0'

        self.tv2.channel_down()
        assert str(self.tv2) == 'Power = True, Channel = 2, Volume = 0'

        self.tv2.channel_down()
        self.tv2.channel_down()
        self.tv2.channel_down()
        assert str(self.tv2) == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        self.tv1.volume_up()
        assert str(self.tv1) == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()

