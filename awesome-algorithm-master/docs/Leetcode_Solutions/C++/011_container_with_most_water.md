#11. container with most water

**<font color=red>�Ѷ�:Medium</font>**

## ˢ������

> ԭ������

*https://leetcode.com/problems/container-with-most-water/
* 
> ��������

```
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
```

## ���ⷽ��

> ˼·
******- ʱ�临�Ӷ�: O(N)******- �ռ临�Ӷ�: O(1)******

�����տ�ʼ�������뵽�ñ����ķ���ȥ�⣬����ʱ�临�Ӷ�Ϊ O(n^2) ����֮������ TLE����ô���Ǿ�Ҫ���㷨�����Ż�������������˫ָ�뷨����������ָ�룬һ��ָ��ͷ����һ��ָ��β�����Ƚ�����ָ��ָ������Ĵ�С����ͷ���Ĵ���ָ��ͷ����ָ������ƶ�һλ����֮����ָ��β����ָ����ǰ�ƶ�һλ��


```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0,j = height.size() - 1,ans = INT_MIN;
		while(i < j)
		{
			int t = min(height[i],height[j]);
			ans = max(ans,t * (j - i));
			height[i] < height[j] ? i++ : j--;
		}
		return ans;
    }
};
```