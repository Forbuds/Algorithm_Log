#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T=10;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int n;
		int cnt = 0;
		cin >> n;
		int arr[1000];
		for (int i = 0;i < n;i++) {
			scanf("%d ", &arr[i]);
		}

		for (int i = 2;i < n-2;i++) 
		{
			int maxH = max(max(arr[i - 2], arr[i - 1]), max(arr[i + 1], arr[i + 2]));
			
			if (maxH < arr[i]) cnt += (arr[i] - maxH);
		}
		printf("#%d %d\n", test_case, cnt);

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}