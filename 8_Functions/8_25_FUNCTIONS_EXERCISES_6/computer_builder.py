def build_computer(motherboard, cpu, memory, **additional_parts):
    print("\n")
    print(f"The computer you have ordered will be build with the following specs...")
    print(f"Motherboard: {motherboard}")
    print(f"CPU: {cpu}")
    print(f"Memory: {memory}")
    for key, value in additional_parts.items():
        print(f"{key}: {value}")