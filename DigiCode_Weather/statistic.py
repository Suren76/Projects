def statistic_for_hours(sensor_dict, api_dict):

    res = dict()

    for i in range(len(sensor_dict["date"])):
        temp = sensor_dict["temp"][i]-api_dict["temp"][i]
        humidity = sensor_dict["humidity"][i]-api_dict["humidity"][i]

        res[f'{int(api_dict["date"][i].split()[0].split("-")[2])}, {int(api_dict["date"][i].split()[1].split(":")[0])}'] = {"temp": temp, "humidity": humidity}

    return res

def statistic_for_days(sensor_dict, api_dict):

    res = dict()

    for i in range(len(sensor_dict["date"])):
        temp = sensor_dict["temp"][i]-api_dict["temp"][i]
        humidity = sensor_dict["humidity"][i]-api_dict["humidity"][i]

        res[f'{int(api_dict["date"][i].split()[0].split("-")[2])}'] = {"temp": temp, "humidity": humidity}

    return res


def summarize_statistic(res_dict):
    temp = 0
    humidity = 0
    for t in res_dict:
        temp += res_dict[t]["temp"]
        humidity += res_dict[t]["humidity"]

    temp = temp/len(res_dict)
    humidity = humidity/len(humidity)

    return temp, humidity
