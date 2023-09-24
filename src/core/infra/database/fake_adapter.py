from core.infra.database.database import DatabaseConnection


class FakeConnection(DatabaseConnection):
    def __init__(self):
        pass

    def init_session(self):
        pass

    def remove_session(self):
        pass
