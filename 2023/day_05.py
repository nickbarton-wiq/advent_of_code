import polars as pl


def get_data():
    with open('2023/day_05.input') as f:
        return f.read().splitlines()


def parse_seeds(data):
    seeds = [int(x) for x in data[0].split(':')[1].strip().split()]
    output = []
    start = 0
    length = 2
    while len(seeds) >= 2:
        start = seeds.pop(0)
        length = seeds.pop(0)
        generated = [x for x in range(start, start + length)]
        output.extend(generated)
    print(output)
    return output


def parse_map_type(data, map_type: str):
    map_type_line_start = 0
    map_type_line_end = 0
    for i, line in enumerate(data):
        if line.startswith(map_type):
            map_type_line_start = i
        if map_type_line_start > 0 and line == '':
            map_type_line_end = i
            break
        if map_type_line_start > 0 and i == len(data)-1:
            map_type_line_end = len(data)
            break

    if map_type_line_start > 0 and map_type_line_end > 0:
        map_type_data = data[map_type_line_start+1:map_type_line_end]
        return [list(map(int, line.split())) for line in map_type_data]
    else:
        print(f"Error: {map_type} not found in data")


def create_mapping(source, destination, almanac, mappings):

    to_be_updated = pl.DataFrame({source: [], destination: []}, schema={source: pl.Int64, destination: pl.Int64})
    for row in almanac.select(pl.col(source)).iter_rows():
        row = row[0]
        for map in mappings:
            source_range_start = map[1]
            destination_range_start = map[0]
            range_length = map[2]

            if row in range(source_range_start, source_range_start + range_length):
                to_be_updated = to_be_updated.vstack(
                    pl.DataFrame(
                        {
                            source: [row],
                            destination: [row + (destination_range_start - source_range_start)],
                        },
                        schema={source: pl.Int64, destination: pl.Int64}
                    )
                )
            # print(to_be_updated)

    almanac = almanac.join(
        to_be_updated,
        on=[source],
        how="left",
    )
    almanac = almanac.with_columns(pl.col(destination)).fill_null(pl.col(source))
    return almanac


def get_max(all_mappings):
    max_number = 0
    for mapping in all_mappings:
        for map in mapping:
            number1 = map[0] + map[2]
            if number1 > max_number:
                max_number = number1
            number2 = map[1] + map[2]
            if number2 > number1 and number2 > max_number:
                max_number = number2
    return max_number


def part1(data):
    # seeds = parse_seeds(data, seeds_to_soil)
    seeds_to_soil = parse_map_type(data, 'seed-to-soil')
    print(seeds_to_soil)
    # soil_to_fertilizer = parse_map_type(data, 'soil-to-fertilizer')
    # fertilizer_to_water = parse_map_type(data, 'fertilizer-to-water')
    # water_to_light = parse_map_type(data, 'water-to-light')
    # light_to_temperature = parse_map_type(data, 'light-to-temperature')
    # temperature_to_humidity = parse_map_type(data, 'temperature-to-humidity')
    # humidity_to_location = parse_map_type(data, 'humidity-to-location')

    # all_mappings = [seeds_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
    #                 temperature_to_humidity, humidity_to_location]

    # max_number = get_max(all_mappings)
    # min_seed = min(seeds)
    # print(min_seed, max_number)

    # df = pl.DataFrame({'seeds': seeds})
    # print(df)
    df = create_mapping('seeds', 'soil', df, seeds_to_soil)
    # print(df)
    # df = create_mapping('soil', 'fertilizer', df, soil_to_fertilizer)
    # # print(df)
    # df = create_mapping('fertilizer', 'water', df, fertilizer_to_water)
    # # print(df)
    # df = create_mapping('water', 'light', df, water_to_light)
    # # print(df)
    # df = create_mapping('light', 'temperature', df, light_to_temperature)
    # # print(df)
    # df = create_mapping('temperature', 'humidity', df, temperature_to_humidity)
    # # print(df)
    # df = create_mapping('humidity', 'location', df, humidity_to_location)
    # # print(df)

    # print(df.with_columns("location").min())


if __name__ == '__main__':
    data = get_data()
    # parse_seeds(data)
    part1(data)

    # seeds = parse_seeds(data)
    # df = pl.from_repr(
    #     """
    #     ┌───────┬──────┬────────────┐
    #     │ seeds ┆ soil ┆ fertilizer │
    #     │ ---   ┆ ---  ┆ ---        │
    #     │ i64   ┆ i64  ┆ i64        │
    #     ╞═══════╪══════╪════════════╡
    #     │ 79    ┆ 81   ┆ 81         │
    #     │ 14    ┆ 14   ┆ 53         │
    #     │ 55    ┆ 57   ┆ 57         │
    #     │ 13    ┆ 13   ┆ 52         │
    #     └───────┴──────┴────────────┘
    #     """
    # )
    # map = create_mapping('fertilizer', 'water', df, [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]])
    # print(map)

    # print(map.filter(pl.col('seeds').is_in([50, 51, 52, 53, 54, 55, 56, 57, 58, 59])))
