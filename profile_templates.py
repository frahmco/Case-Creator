import pickle
from pathlib import Path

class Profile: #Class for Profiles

    def __init__(self = '', firstName = '', lastName = '', agency = '', badgeNumber = '', title = '', casePath = ''):
        self.firstName = firstName
        self.lastName = lastName
        self.agency = agency
        self.badgeNumber = badgeNumber
        self.title = title
        self.defaultCasePath = casePath

    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getAgency(self):
        return self.agency
    def getBadgeNumber(self):
        return self.badgeNumber
    def getTitle(self):
        return self.title
    def getDefaultPath(self):
        return self.defaultCasePath
    
    def setFirstName(self, fN):
        self.firstName = fN
    def setLastName(self, lN):
        self.lastName = lN
    def setAgency(self, a):
        self.agency = a
    def setBadgeNumber(self, bN):
        self.badgeNumber = bN
    def setTitle(self, t):
        self.title = t

    def createProfile(self):
        file = open('profile.pr', 'wb')
        pickle.dump(self, file)
        file.close()

    def readProfile(self):
        file = open('profile.pr', 'rb')
        profile = pickle.load(file)

        return profile

    def profileCheck():
        path = Path('profile.pr')
        if (path.exists()):
            return True
        else:
            return False
