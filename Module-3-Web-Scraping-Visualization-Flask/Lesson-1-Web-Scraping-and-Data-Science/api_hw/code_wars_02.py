def number(bus_stops) -> int:
    #     on, off = 0, 0

    #     for stop in bus_stops:
    #         on += stop[0]
    #         off += stop[1]

    #     return on - off



    #     stops = 0

    #     for stop in bus_stops:
    #         stops += stop[0] - stop[1]

    #     return stops



    return sum(stop[0] - stop[1] for stop in bus_stops)


print(number([[10,0],[3,5],[5,8]])) # => 5
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])) # => 17
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])) # => 21