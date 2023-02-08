import os
class ConcreteUpdateInterceptor:

    UPDATE_LOG_PATH_STRING = str(os.path.abspath('..')) + '/Database/updates.csv'

    def updateLog():
        pass
        #updateDetails = ContextObject()
        #update = updateDetails.updateContext()