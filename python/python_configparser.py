###Config Parser###

import configparser
import os

def create_config(path):
    """Create a config file"""
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)

# if __name__ == "__main__":
#     path = "settings.ini"
#     createConfig(path)

def get_config(path):
    """Return the config object"""
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """Print setting"""
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    print(msg)
    return value

def update_setting(path, section, setting, value):
    """Update a setting"""
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)

def delete_setting(path, section, setting):
    """Delete a setting"""
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "settings.ini"
    font = get_setting(path, 'Settings', 'font')
    font_size = get_setting(path, 'Settings', 'font_size')

    update_setting(path, "Settings", "font_size", "12")

    delete_setting(path, "Settings", "font_style")

# def crudConfig(path):
#     """Create, read, update, delete config"""
#     if not os.path.exists(path):
#         createConfig(path)

#     config = configparser.ConfigParser()
#     config.read(path)

#     #read values from the config
#     font = config.get("Settings", "font")
#     font_size = config.get("Settings", "font_size")
#     print(font, font_size)

#     #change values in the config
#     config.set("Settings", "font_size", "12")

#     #delete values from the config
#     config.remove_option("Settings", "font_style")

#     #write changes to the config
#     with open(path, "w") as config_file:
#         config.write(config_file)

# if __name__ == "__main__":
#     path = "settings.ini"
#     crudConfig(path)

###Interpolation###

def interpolationDemo(path):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get("Settings", "font_info"))

    print(config.get("Settings", "font_info", 
                     vars={"font": "Arial", "font_size": "100"}))
    
if __name__ == "__main__":
    path = "settings.ini"
    interpolationDemo(path)