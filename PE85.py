def find_rect(h, w):
	return trianglar(h) * trianglar(w)
	
def trianglar(n):
	return int(n*(n+1)/2)

h = 53
w = 53
closest_rect = find_rect(h,w)
nsquares = 2000000
while(h > 1):
	temp_rect = find_rect(h - 1, w)
	if temp_rect < nsquares:
		while temp_rect < nsquares:
			w += 1
			temp_rect = find_rect(h - 1, w)
			if abs(temp_rect - nsquares) < abs(closest_rect - nsquares):
				closest_rect = temp_rect
				closest = (h-1, w, closest_rect)
	h -= 1
print(closest)
print(closest[0] * closest[1])

