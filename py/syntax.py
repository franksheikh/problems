# Intersections
def intersection(self, nums: List[List[int]]) -> List[int]:
	seen = set(nums[0])
	for nl in nums[1:]:
		seen &= set(nl)
	return sorted(seen)        