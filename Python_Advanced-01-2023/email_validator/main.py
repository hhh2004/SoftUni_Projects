class NameTooShortError(Exception):
    """Raised when the length of the name in the email is less than or equal to 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Raised when there is no '@' in the email"""
    pass


class InvalidDomainError(Exception):
    """Raised when the domain of the email is invalid"""
    pass


while True:
    email = input()
    if '@' in email:
        name = email.split('@')[0]
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
    else:
        raise MustContainAtSymbolError("Email must contain @")

    if '.' in email:
        domain = email.split('.')[1]
        if domain in ("com", "bg", "org", "net"):
            print("Email is valid")
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
