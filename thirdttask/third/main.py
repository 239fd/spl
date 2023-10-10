filename = "subjects.txt"

subjects_dict = {}

with open(filename, "r") as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) == 2:
            subject = parts[0].strip()
            descriptions = parts[1].strip().split()

            total_lectures = 0

            for description in descriptions:
                try:
                    count = int(description.split("(")[0])
                    total_lectures += count
                except ValueError:
                    pass

            subjects_dict[subject] = total_lectures

print(subjects_dict)
