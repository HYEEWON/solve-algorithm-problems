# Hash Table

from collections import defaultdict
import math

car_in = defaultdict(int)
car_time = defaultdict(int)
car_fee = defaultdict(int)

def calc_time(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []

    for record in records:
        record = record.split()

        if record[2] == 'IN':
            car_in[record[1]] = calc_time(record[0])
        else:
            car_time[record[1]] += (calc_time(record[0]) - car_in[record[1]])
            del car_in[record[1]]

    for k, v in car_in.items():
        car_time[k] += (23 * 60 + 59) - car_in[k]

    for k, v in car_time.items():
        if v <= fees[0]:
            car_fee[k] = fees[1]
        else:
            car_fee[k] = fees[1] + math.ceil((car_time[k]-fees[0]) / fees[2]) * fees[3]

    car_sorted = sorted(car_fee.items(), key=lambda x: x[0])
    for c in car_sorted:
        answer.append(c[1])

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN",
                "23:00 5961 OUT"]))