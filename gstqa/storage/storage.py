# GStreamer QA system
#
#       storage.py
#
# Copyright (c) 2008, Edward Hervey <bilboed@bilboed.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

"""
Classes and methods related to storing/retrieving results/data/...
"""

class DataStorage:
    """
    Base class for storing data
    """
    def __init__(self):
        self.setUp()

    def setUp(self):
        raise NotImplementedError

    # public storage API

    def setClientInfo(self, softwarename, clientname, user):
        pass

    def startNewTestRun(self, testrun):
        # create new entry in testrun table
        pass

    def endTestRun(self, testrun):
        # mark the testrun as closed and done
        pass

    def newTestStarted(self, testrun, test):
        # create new entry in tests table
        pass

    def newTestFinished(self, testrun, test):
        pass

    # public retrieval API
    def listTestRuns(self):
        """
        Returns the list of testruns ID currently available
        """
        pass

    def getTestRun(self, testrunid):
        pass

    def getClientInfoForTestRun(self, testrunid):
        pass

    # methods to implement in subclasses


class FileStorage(DataStorage):
    """
    Base class for storing data to a file

    Don't use this class directly, but one of its subclasses
    """

    def __init__(self, path, *args, **kwargs):
        self.path=path
        DataStorage.__init__(self, *args, **kwargs)

class NetworkStorage(DataStorage):
    """
    Stores data to a remote storage

    Don't use this class directly, but one of its subclasses
    """
    # properties
    # * host
    # * port
    pass

class DBStorage(FileStorage):
    """
    Stores data in a database

    Don't use this class directly, but one of its subclasses
    """

    def setUp(self):
        # open database
        self.openDatabase()

        # createTables if needed
        self.createTables()

    def openDatabase(self):
        raise NotImplementedError

    def createTables(self):
        raise NotImplementedError
