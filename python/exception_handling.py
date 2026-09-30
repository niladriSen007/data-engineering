class InsufficientFundsError(Exception):
    """Raised when a user tries to withdraw more than their balance."""
    # raise ValueError("Invalid Value")
    pass


# Usage
balance = 50
withdraw = 100
if withdraw > balance:
    raise InsufficientFundsError("You do not have enough money!")
