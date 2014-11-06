def CountWidgetByType(iniFile, searchString):
    import configparser
    Config = configparser.ConfigParser()
    Config.read(iniFile)

    # Initialize counter
    Count = 0

    # Count each of the various types of entries in the INI file
    for section in Config.sections():
        foundPointer = section.find(searchString)
        if foundPointer != -1:
            Count = Count + 1
        pass
    pass

    # Return results
    return Count