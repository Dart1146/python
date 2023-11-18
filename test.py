class Television:
    """

    Attributes:
        __muted (bool): Indicates whether the TV is muted or not.
        __volume (int): The current volume level.
        __channel (int): The current channel.
        __status (bool): Indicates whether the TV is powered on or off.

    Class Constants:
        MIN_VOLUME (int): The minimum volume level.
        MAX_VOLUME (int): The maximum volume level.
        MIN_CHANNEL (int): The minimum channel number.
        MAX_CHANNEL (int): The maximum channel number.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a tv object with default values.
        """
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__status: bool = False

    def power(self) -> None:
        """
        Method to toggle the power status on the tv.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to toggle the mute status on the tv.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        method to increase the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to show the tv status.

        :return: tv status.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
