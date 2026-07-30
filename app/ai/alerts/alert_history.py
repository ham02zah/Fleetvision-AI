class AlertHistory:

    _alerts = []

    @classmethod
    def add(

        cls,

        alert,

    ):

        cls._alerts.append(alert)

    @classmethod
    def all(cls):

        return cls._alerts

    @classmethod
    def clear(cls):

        cls._alerts = []