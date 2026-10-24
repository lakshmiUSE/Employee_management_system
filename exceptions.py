class EmployeeManagementError(Exception):
    """Base exception for the application."""
    pass


class EmployeeNotFoundError(EmployeeManagementError):
    """Raised when an employee does not exist."""
    pass


class DuplicateEmployeeError(EmployeeManagementError):
    """Raised when an employee ID or email already exists."""
    pass


class ValidationError(EmployeeManagementError):
    """Raised when employee information is invalid."""
    pass


class DataStorageError(EmployeeManagementError):
    """Raised when employee data cannot be read or saved."""
    pass
