def iga():
    car_list = [
        {
            "car_id": 1,
            "color": "red",
            "data": "Cost: 20000"
        },
        {
            "car_id": 2,
            "color": "red",
            "data": "Cost: 30000"
        },
        {
            "car_id": 3,
            "color": "yellow",
            "data": "Cost: 30000"
        }
    ]
    r=calc_total_cost(car_list)
    print(r)



def calc_total_cost(car_list):
    cost=''

    for i in car_list:
        cost += (str(i["data"]))
        return cost
