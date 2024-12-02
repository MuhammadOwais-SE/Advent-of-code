# readlines make the each line into string 
# e.g "99006   28305\n" To remove "\n" we need to use strip() in the loop 
# and s aved the data into the new list.
# convert string in integer using map function and then convert into list
lines = [list(map(int, line.strip().split())) for line in open("input.txt", "r").readlines()]

# part 1
def check_report(report):

    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

    valid_differ = all(1<= abs(report[i]-report[i+1]) <= 3 for i in range(len(report)-1))

    return(increasing or decreasing) and valid_differ


def damper_safe(report):
    if check_report(report):
        return True
    
    # Try removing each level and check if the remaining report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if check_report(modified_report):
            return True
    return False


safe_count = sum(1 for reports in lines if check_report(reports))
safe_damper_count = sum(1 for reports in lines if damper_safe(reports))

# for reports in lines:
#     print(f"Report {reports} is {'Safe' if check_report(reports) else 'Unsafe' }")

# part 1
print(f"Total safe count is: {safe_count}")
# part 2
print(f"Total safe count using damper is: {safe_damper_count}")