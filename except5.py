class VotingError(Exception):
    pass

class LessAgeVotingError(VotingError):
    pass

class MoreAgeVotingError(VotingError):
    pass

print("before error")

age = int(input("Please enter your age "))

try:
    if age<18:
        raise LessAgeVotingError
    else:
        raise MoreAgeVotingError
except LessAgeVotingError as err:
    print("Age is less.")
except MoreAgeVotingError as err:
    print("Age is more.")

print("after error")