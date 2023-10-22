class CPFException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidCPF(CPFException):
    def __init__(self, message):
        super().__init__(message)


class CPFAlreadyExists(CPFException):
    def __init__(self, message):
        super().__init__(message)


class DatabaseInstanceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class EmployeeNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class EmployeeUpdateException(Exception):
    def __init__(self, message):
        super().__init__(message)
