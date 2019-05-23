# -*- coding: utf-8 -*-

def merge_sort(l_a, start, end ):
	if(start >= end):
		return

	mid = (start + end)/2
	merge_sort(l_a, start, mid)
	merge_sort(l_a, mid+1, end)

	return merge_sort_d(l_a, mid, start, end )

def merge_sort_d(l_a, mid, start, end):

	l_tmp=[]
	l = mid+1
	i = start

	while(i <= mid and l <= end ):
	# 谁小放谁
		if(l_a[i] <= l_a[l]):
			l_tmp.append(l_a[i])
			i=i+1

		else:
			l_tmp.append(l_a[l])
			l=l+1

	# 哪边有剩余，就把哪边的数据插入到数组，有且只有一边会有剩余
	while(i <= mid):
		l_tmp.append(l_a[i])
		i=i+1

	while(l <= end):
		l_tmp.append(l_a[l])
		l=l+1

	it = 0 
	while(it < len(l_tmp)):
		l_a[start+it] = l_tmp[it]
		it=it+1

l_a = [9, 8, 1, 4, 5, 2, 3, 6, 7, 8]
start = 0
end = len(l_a) - 1

print "test data"
print l_a

l_a_af = merge_sort(l_a, start, end)
print "after sort data"
print l_a