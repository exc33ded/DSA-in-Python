import collections

def find_max_frequency(arr, N, K, X):
  # Find element with highest initial frequency
  max_element, max_count = max([(a, c) for a, c in collections.Counter(arr).items()])

  # Iterate through the array and update max potential frequency
  for i in range(N):
    current_num = arr[i]
    for new_num in range(current_num - X, current_num + X + 1):
      # Calculate potential frequency gain by replacing with highest count element
      gain = collections.Counter(arr)[new_num] - collections.Counter(arr)[current_num]
      # Update max potential frequency if beneficial and operations remain
      if gain > 0 and K > 0:
        # Avoid exceeding actual achievable frequency by adding gain to min of current max and initial count of replaced element
        max_count = min(max_count + gain, collections.Counter(arr)[current_num] + K)
        K -= 1

  return max_count

# Example usage
arr = [1, 2, 3, 4]
N = len(arr)
K = 2
X = 2

max_freq = find_max_frequency(arr, N, K, X)
print("Maximum achievable frequency:", max_freq)
