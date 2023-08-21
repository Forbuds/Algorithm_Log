# [Silver III] 구간 합 구하기 4 - 11659 

[문제 링크](https://www.acmicpc.net/problem/11659) 

### 성능 요약

메모리: 41316 KB, 시간: 264 ms

### 분류

누적 합

### 문제 설명

<p>수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.</p>

### 출력 

 <p>총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.</p>

[구간합 시간 복잡도: O(nm)](https://hongcoding.tistory.com/159#:~:text=%EC%B4%9D%20%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84%EB%8A%94%20O,%EC%B4%88%EA%B3%BC%20%EC%98%A4%EB%A5%98%EA%B0%80%20%EB%82%98%EA%B2%8C%20%EB%90%9C%EB%8B%A4.)
[수행 제한 시간: O(n+m)](https://freedeveloper.tistory.com/394) 이렇게 때문에 DP처럼 코드를 짠다.
이론 이름은 Prefix Sum (접두사 합)
