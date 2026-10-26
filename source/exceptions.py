
class EmployeeManagementError(Exception):
    """Base exception for employee management."""
    pass





class ValidationError(EmployeeManagementError):
    """Raised when employee data is invalid."""
    pass

class DuplicateEmployeeError(EmployeeManagementError):
    """Raised when an employee already exists."""
    pass


class DataStorageError(EmployeeManagementError):
    """Raised when employee data cannot be read or saved."""
    pass
