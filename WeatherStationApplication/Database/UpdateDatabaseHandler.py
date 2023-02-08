import csv
class UpdateDatabaseHandler:
    
    updateLogString = 'WeatherStationApplication/Database/updates.csv'

    def getNewestUpdateId():
        with open('WeatherStationApplication/Database/updates.csv') as f:
            updateDict = csv.DictReader(f)