# Problem A - Avoiding accidents

translated by Google Translation

You have a collection of four-character words on your desk. However, your friends and their little child are visiting you next week. If the toddler finds and tries to eat your words, it may choke on them and die. To prevent such an accident, you want to hide your words into a single longer string that won’t fit into the baby’s mouth.

책상에 네 자의 단어가 모여 있습니다. 그러나 친구와 자녀는 다음 주에 당신을 방문합니다. 아이가 당신의 말을 찾아서 먹으려고하면, 그 아이가 말라 죽을 수도 있습니다. 이러한 사고를 방지하기 위해 단어를 아기의 입에 맞지 않는 긴 문자열 하나에 숨기려고합니다.

![a_pic.png](https://ipsc.ksp.sk/2016/real/problems/a_pic.png)


## Problem specification

You are given exactly ten strings. Each of them consists of exactly four characters. Construct a new string of length exactly n which contains all ten given words as substrings.

정확히 10 개의 문자열이 주어집니다. 각각 정확히 4 자로 구성됩니다. 지정된 10 개의 단어를 모두 하위 문자열로 포함하는 길이가 정확히 n 인 새 문자열을 구성합니다.

Each substring must be contiguous. For example, ABXCD does not contain ABCD as a substring. The occurrences of the ten given strings may appear in any order and they may overlap arbitrarily.

각 부분 문자열은 인접해야합니다. 예를 들어, ABXCD는 부분 문자열로 ABCD를 포함하지 않습니다. 주어진 열 10 개가 임의의 순서로 나타날 수 있으며 임의로 겹칠 수 있습니다.

This problem has two independent subproblems:

이 문제는 두 가지 독립적인 하위 문제가 있습니다.

* In the easy subproblem A1 you have to produce a string of length n = 42.
* 쉬운 하위 문제 A1에서 길이 n = 42의 문자열을 생성해야합니다.
* In the hard subproblem A2 you have to produce a string of length n = 39.
* 어려운 하위 문제 A2에서는 길이 n = 39의 문자열을 생성해야합니다.

## Input specification

The first line of the input file contains an integer t specifying the number of test cases. Each test case is preceded by a blank line. Each test case consists of exactly ten space-separated strings. Each string consists of exactly four UPPERCASE English letters (from A to Z).

입력 파일의 첫 번째 줄에는 테스트 사례의 수를 지정하는 정수 t가 포함됩니다. 각 테스트 케이스 앞에 빈 줄이옵니다. 각 테스트 케이스는 정확히 10 개의 공백으로 구분 된 문자열로 구성됩니다. 각 문자열은 정확히 대문자 영문자 (A에서 Z까지)로 구성됩니다.

## Output specification

For each test case, print a single line with a string of UPPERCASE letters. Each of given ten words must appear in your string as a substring at least once. The length of the string must be exactly 42 if you are solving the easy subproblem, and it must be exactly 39 if you are solving the hard subproblem.

각 테스트 케이스에 대문자 문자열이있는 한 줄을 인쇄하십시오. 주어진 10 개의 단어 각각은 최소한 한 번만 하위 문자열로 문자열에 나타나야합니다. 쉬운 하위 문제를 해결하려면 문자열의 길이는 정확히 42 여야하며 어려운 하위 문제를 해결하는 경우 문자열의 길이는 정확히 39 여야합니다.

The inputs are chosen in such a way that a solution always exists. If there are multiple solutions, you may choose and output any one of them.

입력은 솔루션이 항상 존재하는 방식으로 선택됩니다. 솔루션이 여러 개인 경우 해당 솔루션을 선택하여 출력 할 수 있습니다.

## What to submit

Do not submit any programs. Your task is to produce and submit the correct output files a1.out and a2.out for the provided input files a1.in and a2.in. Each line in the file a1.out must contain a 42-character string. Each line in the file a2.out must contain a 39-character string.

어떤 프로그램도 제출하지 마십시오. 당신의 임무는 제공된 입력 파일 인 a1.in과 a2.in에 대해 올바른 출력 파일 인 a1.out과 a2.out을 생성하여 제출하는 것입니다. 파일 a1.out의 각 행에는 42 자 문자열이 있어야합니다. 파일 a2.out의 각 행에는 39 자 문자열이 있어야합니다.

## Example

Here is one possible input file:

### Input:

```
2

TEST INTE RNET PROB ROBL OBLE BLEM SOLV VING TEST

AAAA AAAA AAAA AAAA AAAA AAAA AAAA AAAA AAAA AAAA
```

If n were 29, this would be one possible correct output:

### Output:

```
INTERNETPROBLEMSOLVINGCONTEST
AAAAAAAAAAAAAAAAAAAHELLOWORLD
```