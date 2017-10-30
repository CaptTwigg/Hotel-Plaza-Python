class Guest(object):
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

    def toString(self):
        # return self.firstName + " " + self.lastName + " " + self.phoneNumber
        return "{0.firstName} {0.lastName} {0.phoneNumber}".format(self)
