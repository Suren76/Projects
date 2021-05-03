from datetime import datetime


def statistic_for_hours(sensor_dict, api_dict):

    res = dict()

    for i in range(len(sensor_dict["date"])):
        print(i)
        temp = abs(int(sensor_dict["temp"][i])-int(api_dict["temp"][i]))
        humidity = abs(int(sensor_dict["humidity"][i])-int(api_dict["humidity"][i]))
        print(f'{str(datetime.now().time()).split(".")[0]}:: temp: {sensor_dict["temp"][i]}, humidity: {sensor_dict["humidity"][i]}')
        print(f'{str(datetime.now().time()).split(".")[0]}:: temp: {api_dict["temp"][i]}, humidity: {api_dict["humidity"][i]}')
        res[str(str(datetime.now().time()).split(".")[0])] = {"temp": temp, "humidity": humidity}

    return res


def summarize_statistic(res_dict):
    temp = 0
    humidity = 0
    for t in res_dict:
        temp += int(res_dict[t]["temp"])
        humidity += int(res_dict[t]["humidity"])
    print(len(res_dict))
    temp = temp/len(res_dict)
    humidity = humidity/len(res_dict)

    return {"temp": temp, "humidity": humidity}


# def statistic_for_hours_swap(sensor_dict, api_dict):

#     res = dict()

#     for i in range(len(sensor_dict["date"])):
#         temp = sensor_dict["temp"][i]-api_dict["temp"][i]
#         humidity = sensor_dict["humidity"][i]-api_dict["humidity"][i]

#         res[f'{int(api_dict["date"][i].split()[0].split("-")[2])}, {int(api_dict["date"][i].split()[1].split(":")[0])}'] = {"temp": temp, "humidity": humidity}

#     return res