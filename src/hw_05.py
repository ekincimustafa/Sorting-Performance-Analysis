import os
# Custom pseudorandom number generator with a random initial seed
class PRNG:
    def __init__(self, seed=None):
        # Use a truly random seed if no seed is provided
        if seed is None:
            seed = int.from_bytes(os.urandom(4), 'big')  # Generate a random 32-bit integer
        self.state = seed

    def randint(self, low, high):
        # Simple linear congruential generator (LCG)
        self.state = (1103515245 * self.state + 12345) % (2**31)
        return low + (self.state % (high - low + 1))

# Generate logistics dataset
def generate_logistics_dataset(num_warehouses=100, max_packages=1000, seed=None):
    """Generates a logistics dataset with a random or specified seed."""
    prng = PRNG(seed)  # Initialize PRNG with the seed or a random one
    data = []
    for i in range(1, num_warehouses + 1):
        warehouse_id = f"WH-{str(i).zfill(3)}"
        priority_level = prng.randint(1, 5)
        package_count = prng.randint(0, max_packages)
        data.append([warehouse_id, priority_level, package_count])
    return data

# Save dataset to a CSV file
def save_to_csv(data, file_name):
    """Saves the dataset to a CSV file."""
    with open(file_name, "w") as file:
        # Write the header
        file.write("Warehouse_ID,Priority_Level,Package_Count\n")
        # Write each row
        for row in data:
            file.write(",".join(map(str, row)) + "\n")


######### YOUR CODE GOES HERE ---  You should define here two_level_sorting and the 3 sorting functions

### Your three sorting functions should have global variable named as counter. So do not return it.
def bubble_sort(dataset):

    bubble_sort_pl_iterations = 0
    bubble_sort_pc_iterations = 0

    dataset_copy = dataset[:]

    n = len(dataset_copy)

    for i in range(n):
        for j in range(0, n - i - 1):
            bubble_sort_pl_iterations += 1
            if dataset_copy[j][1] > dataset_copy[j + 1][1]:
                dataset_copy[j], dataset_copy[j + 1] = dataset_copy[j + 1], dataset_copy[j]

    i = 0
    while i < n:
        j = i + 1
        while j < n and dataset_copy[i][1] == dataset_copy[j][1]:
            j += 1

        if j - i > 1:
            for k in range(i, j):
                for l in range(i, j - (k - i) - 1):
                    bubble_sort_pc_iterations += 1
                    if dataset_copy[l][2] > dataset_copy[l + 1][2]:
                        dataset_copy[l], dataset_copy[l + 1] = dataset_copy[l + 1], dataset_copy[l]
        i = j

    bubble_sorted = dataset_copy
    return bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations

def merge_sort(dataset_copy_2, index, counter):

    if len(dataset_copy_2) <= 1:
        return dataset_copy_2

    mid = len(dataset_copy_2) // 2
    left_half = dataset_copy_2[:mid]
    right_half = dataset_copy_2[mid:]

    sorted_left = merge_sort(left_half, index, counter)
    sorted_right = merge_sort(right_half, index, counter)

    def merge(left, right, index, counter):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i][index] <= right[j][index]:

                result.append(left[i])
                i += 1
            else:
                counter[0] += 1
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


    return merge(sorted_left, sorted_right, index, counter)


def quick_sort(dataset_copy_3, counter, index):

    if len(dataset_copy_3) <= 1:
        return dataset_copy_3

    pivot = dataset_copy_3[len(dataset_copy_3) // 2]
    counter[0] += 1

    def quick_sort_1(dataset_copy_3, pivot, index, counter):

        above = []
        under = []
        equal = []

        for i in dataset_copy_3:
            if i[index] > pivot[index]:
                above.append(i)
            elif i[index] < pivot[index]:
                under.append(i)
            else:
                equal.append(i)

        if index == 2:
            counter[1] += 1

        return above, under, equal

    above, under, equal = quick_sort_1(dataset_copy_3, pivot, index, counter)

    sorted_above = quick_sort(above, counter, index)
    sorted_under = quick_sort(under, counter, index)

    quick_sorted = sorted_under + equal + sorted_above

    return quick_sorted


def two_level_sorting(functions, dataset):

    counter = [0, 0]


    if functions == bubble_sort:
        dataset_copy_1 = dataset[:]
        bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations = bubble_sort(dataset_copy_1)
        return bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations

    elif functions == merge_sort:
        dataset_copy_2 = dataset[:]
        merge_sorted_1 = merge_sort(dataset_copy_2, 1, counter)

        def group_by_second_element(dataset):
            grouped_data = {}
            for row in dataset:
                if row[1] not in grouped_data:
                    grouped_data[row[1]] = []
                grouped_data[row[1]].append(row)
            return grouped_data

        grouped_data = group_by_second_element(merge_sorted_1)

        sorted_data = []
        for group in grouped_data.values():
            if len(group) > 1:
                sorted_group = merge_sort(group, 2, counter)
                sorted_data.extend(sorted_group)
            else:
                sorted_data.extend(group)

        return sorted_data, counter[0], counter[1]

    if functions == quick_sort:
        dataset_copy_3 = dataset[:]

        quick_sorted_1 = quick_sort(dataset_copy_3, counter, 1)

        def group_by_second_element(dataset):
            grouped_data = {}
            for row in dataset:
                if row[1] not in grouped_data:
                    grouped_data[row[1]] = []
                grouped_data[row[1]].append(row)
            return grouped_data

        grouped_data = group_by_second_element(quick_sorted_1)

        sorted_data = []
        for group in grouped_data.values():
            if len(group) > 1:
                sorted_group = quick_sort(group, counter, 2)
                sorted_data.extend(sorted_group)
            else:
                sorted_data.extend(group)

        return sorted_data, counter[0], counter[1]


#########

def write_output_file(
    bubble_sorted, merge_sorted, quick_sorted,
    bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
    bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
    merge_check, quick_check
):
    """Write sorted results and comparisons to the output file."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write("=== Bubble Sorted Results ===\n")
        # file.write(bubble_sorted.to_string() + "\n\n")
        file.write("Warehouse_ID  Priority_Level  Package_Count\n")
        file.write("-" * 40 + "\n")
        for row in bubble_sorted:
            file.write(f"{row[0]:<12}  {row[1]:<14}  {row[2]:<13}\n")
        file.write("\n")
        file.write("=== Comparison Results ===\n")
        if merge_check:
            file.write("Merge and Bubble sorts are identical.\n")
        else:
            file.write("Merge and Bubble sorts differ.\n")
        
        if quick_check:
            file.write("Quick and Bubble sorts are identical.\n")
        else:
            file.write("Quick and Bubble sorts differ.\n")
        
        file.write("\n=== Sort Performance Metrics ===\n")
        file.write(f"Bubble priority sort iteration count: {bubble_sort_pl_iterations}\n")
        file.write(f"Merge priority sort n_of right array is smaller than left: {merge_sort_pl_counter}\n")
        file.write(f"Quick priority sort recursive step count: {quick_sort_pl_counter}\n\n")
        
        file.write(f"Bubble package count sort iteration count: {bubble_sort_pc_iterations}\n")
        file.write(f"Merge package count n_of right array is smaller than left: {merge_sort_pc_counter}\n")
        file.write(f"Quick package count sort recursive step count: {quick_sort_pc_counter}\n")
    
    print(f"Results written to {OUTPUT_FILE}")
    
if __name__ == "__main__":
    # File paths and dataset size
    # Specify paths for input and output files
    INPUT_FILE = "C:\\"   # Path where the generated dataset will be saved
    OUTPUT_FILE = "C:\\"  # Path where the sorted results and metrics will be saved
    SIZE = 10  # Number of warehouses in the dataset

    # Generate the dataset
    dataset = generate_logistics_dataset(SIZE, max_packages=100)  # Generate a dataset with SIZE warehouses and max_packages packages
    
    # Save the generated dataset to the input file
    save_to_csv(dataset, INPUT_FILE)
    
    
    ###############################################################################################################
    # Perform sorting and counting operations
    # Sort using Bubble Sort and count iterations for Priority Level (_pl_) and Package Count (_pc_)
    bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations = two_level_sorting(bubble_sort, dataset)
    
    # Sort using Merge Sort and count recursive steps for Priority Level and Package Count
    merge_sorted, merge_sort_pl_counter, merge_sort_pc_counter = two_level_sorting(merge_sort, dataset)
    
    # Sort using Quick Sort and count recursive steps for Priority Level and Package Count
    quick_sorted, quick_sort_pl_counter, quick_sort_pc_counter = two_level_sorting(quick_sort, dataset)
    ###############################################################################################################
    
    
    # Comparisons
    # Check if Merge Sort results match Bubble Sort results
    merge_check = merge_sorted == bubble_sorted

    # Check if Quick Sort results match Bubble Sort results
    quick_check = quick_sorted == bubble_sorted

    # Write results and metrics to the output file
    write_output_file(
        bubble_sorted, merge_sorted, quick_sorted,
        bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
        bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
        merge_check, quick_check
    )


   
