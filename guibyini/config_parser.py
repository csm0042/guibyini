def ConfigSectionMap(INIfile, section, key):
    import configparser
    Config = configparser.ConfigParser()
    Config.read(INIfile)
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                logging.info('Skip: %s' % option)
        except:
            logging.info('Exception on %s' % option)
            dict1[option] = None
    return dict1[key]