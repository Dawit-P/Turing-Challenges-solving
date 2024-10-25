def bubble_sort(ps):
    # Outer loop for each pass
    for pass_number in range(len(ps) - 1):  # len(ps) - 1 passes are needed
        # Inner loop to compare adjacent elements
        for i in range(len(ps) - 1 - pass_number):
            # Compare the current element with the next
            if ps[i] > ps[i + 1]:
                # Swap if the current element is greater than the next element
                ps[i], ps[i + 1] = ps[i + 1], ps[i]
                print(f"Swapped {ps[i+1]} with {ps[i]}: {ps}")  # Debug output

    print("Sorted list:", ps)  # Final output

# Test the function
ps = [5, 2, 9, 1, 5, 6]
bubble_sort(ps)
