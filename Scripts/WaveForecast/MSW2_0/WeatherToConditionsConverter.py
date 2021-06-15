#Converts number of weather icon status to description

def convertWeather(weatherConditionNum):
    if(weatherConditionNum == str(1)):
        return "Sunny"
    elif(weatherConditionNum == str(2)):
        return "Partly Cloudy"
    elif(weatherConditionNum == str(3)):
        return "Partly Cloudy with Light Showers"
    elif(weatherConditionNum == str(4)):
        return "Partly Cloudy with Light Showers"
    elif(weatherConditionNum == str(5)):
        return "Partly Cloudy with Light Showers and Snow"
    elif(weatherConditionNum == str(6)):
        return "Partly Cloudy with Stars"
    elif(weatherConditionNum == str(7)):
        return "Partly Cloudy With Light Snow"
    elif(weatherConditionNum == str(8)):
        return "Partly Cloudy with Heavy Snow"
    elif(weatherConditionNum == str(9)):
        return "ThuderStorm"
    elif(weatherConditionNum == str(10)):
        return "Dark Skys"
    elif(weatherConditionNum == str(11)):
        return "Cloudy Dark Skys"
    elif(weatherConditionNum == str(12)):
        return "Dark Skys With Light Showers"
    elif(weatherConditionNum == str(13)):
        return "Dark Skys With Showers"
    elif(weatherConditionNum == str(14)):
        return "Dark Skys With Showers and Snow"
    elif(weatherConditionNum == str(15)):
        return "Dark Skys With Stars"
    elif(weatherConditionNum == str(16)):
        return "Dark Skys With Snow"
    elif(weatherConditionNum == str(17)):
        return "Dark Skys With Heavy Snow"
    elif(weatherConditionNum == str(18)):
        return "Dark Skys with ThunderStorm"
    elif(weatherConditionNum == str(19)):
        return "Cloudy"
    elif(weatherConditionNum == str(20)):
        return "Rain Clouds"
    elif(weatherConditionNum == str(21)):
        return "Heavy Showers"
    elif(weatherConditionNum == str(22)):
        return "Light Showers"
    elif(weatherConditionNum == str(23)):
        return "Heavy Showers"
    elif(weatherConditionNum == str(24)):
        return "Light Showers with Snow"
    elif(weatherConditionNum == str(25)):
        return "Cloudy With Stars"
    elif(weatherConditionNum == str(26)):
        return "Cloudy with Snow"
    elif(weatherConditionNum == str(27)):
        return "Heavy Snow"
    elif(weatherConditionNum == str(28)):
        return "ThunderStorm"
    elif(weatherConditionNum == str(29)):
        return "Very Heavy Showers"
    elif(weatherConditionNum == str(30)):
        return "Clear Skys"
    elif(weatherConditionNum == str(31)):
        return "Gray Skys"
    elif(weatherConditionNum == str(32)):
        return "Orange Skys"
    elif(weatherConditionNum == str(33)):
        return "Cloudy with Light Snow"
    elif(weatherConditionNum == str(34)):
        return "Partly Cloudy with Light Showers"
    elif(weatherConditionNum == str(35)):
        return "Partly Cloudy with Light Snow"
    elif(weatherConditionNum == str(36)):
        return "Lightning"
    elif(weatherConditionNum == str(37)):
        return "Dark Skys with Light Showers"
    elif(weatherConditionNum == str(38)):
        return "Dark Skys with Light Snow"
    return ""
    
def convertToMessage(weatherConditionNum):
    condition = convertWeather(weatherConditionNum)
    if(condition!=""):
        condition = ', '+str(condition)
    return condition