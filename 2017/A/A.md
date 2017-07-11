# Automated flooding

You are playing a computer game in which your goal is to flood the whole world.

The world is an r × c rectangle divided into unit square cells. Currently, all cells are dry. The game has two separate phases:

* In the first phase, you can use your mouse to flood some individual cells. Whenever you click a cell, it becomes a water cell. When you’re done with clicking, you can start the second phase.
* In the second phase you just wait for the water to spread. Water spreads in steps. In each step, each dry cell that shares a side with at least two different water cells changes into a water cell.

당신은 당신의 목표가 전 세계를 홍수로 삼는 컴퓨터 게임을하고 있습니다.

세계는 단위 사각형 셀로 분할 된 r x c 사각형입니다. 현재 모든 세포는 건조한 상태입니다. 이 게임은 두 가지 단계로 구분됩니다.

* 첫 번째 단계에서는 마우스를 사용하여 일부 개별 셀을 범람시킬 수 있습니다. 세포를 클릭 할 때마다 물 세포가됩니다. 클릭이 끝나면 두 번째 단계를 시작할 수 있습니다.
* 두 번째 단계에서는 물이 퍼지기를 기다립니다. 물이 단계적으로 퍼집니다. 각 단계에서 적어도 두 개의 서로 다른 물 세포가있는면을 공유하는 각 건조한 세포가 물 세포로 바뀝니다.

## Problem specification

You are given the dimensions of the world. Flood the entire world using as few clicks as possible.

당신에게는 세계의 차원이 주어집니다. 가능한 한 적은 클릭을 사용하여 전 세계에 홍수를 퍼붓습니다.

## Input specification

The first line of the input file contains an integer `t` specifying the number of test cases. Each test case is preceded by a blank line.

Each test case consists of a single line with two positive integers r and c: the dimensions of the world. The individual cells of the world have coordinates ranging from (0, 0) to (r − 1, c − 1).

You may assume that t = 100 and that 1 ≤ r, c ≤ 100.

In the easy subproblem A1 you may also assume that r = c (i.e., the world is a square).

## Output specification

For each test case output a block of lines. The first line of the block should contain the number x of clicks you should make. Each of the following x lines should contain the coordinates of a cell you should click. There are usually multiple optimal solutions. We will accept any of them.

각 테스트 케이스에 대해 한 줄의 블록을 출력하십시오. 블록의 첫 번째 줄에는 클릭 수 x가 있어야합니다. 다음 x 줄은 각각 클릭해야하는 셀의 좌표를 포함해야합니다. 보통 여러 최적의 솔루션이 있습니다. 우리는 그 중 하나를 받아 들일 것입니다.

## What to submit

Do not submit any programs. Your task is to produce and submit the correct output files a1.out and a2.out for the provided input files a1.in and a2.in.

## Example

### Input:

```
2

2 2

3 4
```

### Output:

```
2
0 1
1 0
4
0 0
0 2
2 2
2 3
```

The second sample output is illustrated below, with ‘W’ denoting a water cell and ‘.’ denoting a dry cell. On the left is the state of the world just after you made the four clicks. Progressing towards the right you see how the water spreads until it floods the entire world.

두 번째 샘플 출력은 아래 그림과 같으며 'W'는 물 셀을 나타내고 '.'는 건전지를 나타냅니다. 왼쪽에는 4 클릭을 한 직후의 세계 상태가 표시됩니다. 오른쪽으로 진행하면 전 세계에 홍수가 날 때까지 물의 퍼짐을 볼 수 있습니다.

```
        W.W.        WWW.        WWW.        WWWW        WWWW
        ....   ->   ..W.   ->   .WWW   ->   WWWW   ->   WWWW
        ..WW        ..WW        ..WW        .WWW        WWWW
```
