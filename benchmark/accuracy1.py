def calculate_accuracy(expected, predicted):
    total = len(expected)
    correct = 0
    for key in expected:
        if key in predicted:
            if expected[key] == predicted[key]:
                correct += 1
    return round((correct/total)*100, 2)

expected = {
    "name":"John",
    "email":"john@gmail.com",
    "phone":"9876543210"
}

predicted = {
    "name":"John",
    "email":"john@gmail.com",
    "phone":"9876543211"
}

print(calculate_accuracy(expected,predicted))