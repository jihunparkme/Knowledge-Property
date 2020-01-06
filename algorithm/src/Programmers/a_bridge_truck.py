def solution(bridge_length, weight, truck_weights):
    a_bridge_truck = []
    travel_distance = []
    arrived_truck = []
    answer = 0

    while not(truck_weights == [] and travel_distance == []):
        if truck_weights != []:
            a_bridge_truck.append(truck_weights[0])
            if sum(a_bridge_truck) <= weight:
                del truck_weights[0]
                travel_distance.append(0)  # 1만큼 이동
            else : del a_bridge_truck[len(a_bridge_truck)-1]

        answer += 1
        travel_distance = list(map(lambda x : x+1, travel_distance))

        if travel_distance[0] == bridge_length:
            arrived_truck.append(a_bridge_truck[0])
            del a_bridge_truck[0]
            del travel_distance[0]

    return answer+1

if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))