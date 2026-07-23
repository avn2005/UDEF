data = extractor.extract(text)

errors = validate_data(data)

if errors:
    print(errors)
else:
    print("Validation Successful")