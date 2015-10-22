# Python JSON to CSV - bad encoding, UnicodeDecodeError: 'charmap' codec can't decode byte
with open(args.input_file, 'r', encoding="cp866") as input_file:
        data = input_file.read()
        structure = json.loads(data)
