seat_type = input(f"Please neter your seat choice(luxury/ac/sleeper/general): ").lower()

match seat_type:
    case "luuxury":
        print(f"luxury seat")
    case "ac":
        print(f"beds, ac")
    case "sleeper":
        print(f"beds, no ac")
    case "general":
        print(f"no beds, no ac, chair")
    case _:
        print(f"Invalid Choice!")    