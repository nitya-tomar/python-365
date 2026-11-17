def get_errors_from_file(filename):
    errors = []
    with open(filename, "r") as f:       # "r" = read mode
        for i in f:
            parts = i.strip().split(",")   # strip() end ka \n hata deta hai
            if parts[2] == "ERROR":
                errors.append(parts[1] + " - " + parts[3])
    return errors

print(get_errors_from_file("app.log"))