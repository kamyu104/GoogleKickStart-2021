# [GoogleKickStart 2021](https://codingcompetitions.withgoogle.com/kickstart) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-12%20%2F%2012-ff69b4.svg)

Python solutions of Google Kick Start 2021. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

* [Kick Start 2020](https://github.com/kamyu104/GoogleKickStart-2020)
* [Round A](https://github.com/kamyu104/GoogleKickStart-2021#round-a)
* [Round B](https://github.com/kamyu104/GoogleKickStart-2021#round-b)
* [Round C](https://github.com/kamyu104/GoogleKickStart-2021#round-c)

## Round A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [K-Goodness String](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3)| [Python](./Round%20A/k_goodness_string.py)| _O(N)_ | _O(1)_ | Easy | | String |
|B| [L Shaped Plots](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509)| [Python](./Round%20A/l_shaped_plots.py) | _O(R * C)_ | _O(min(R, C))_ | Easy | | DP |
|C| [Rabbit House](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14)| [Python](./Round%20A/rabbit_house.py)| _O(R * C)_ | _O(R * C)_ | Medium | | Bucket Sort, BFS |
|D| [Checksum](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3)| [Python](./Round%20A/checksum.py) | _O(N^2)_ | _O(N^2)_ | Hard | | MST, Prim's Algorithm |

## Round B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Increasing Substring](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882)| [Python](./Round%20B/increasing_substring.py)| _O(N)_ | _O(1)_ | Easy | | String |
|B| [Longest Progression](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509)| [Python](./Round%20B/longest_progression.py) [Python](./Round%20B/longest_progression2.py) | _O(N)_ | _O(1)_ | Medium | | DP |
|C| [Consecutive Primes](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6)| [Python](./Round%20B/consecutive_primes.py)| _O(N^(1/4) * MAX_GAP)_ | _O(1)_ | Medium | | Math, Prime Gap |
|D| [Truck Delivery](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a885)| [PyPy](./Round%20B/truck_delivery.py) | _O((N + Q) * (logN + log(MAX_A)))_ | _O(N)_ | Hard | | DFS, Segment Tree |

## Round C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Smaller Strings](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e)| [Python](./Round%20C/smaller_strings.py)| _O(N)_ | _O(1)_ | Easy | | Math, Counting |
|B| [Alien Generator](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb)| [Python](./Round%20C/alien_generator.py) | _O(sqrt(G))_ | _O(1)_ | Easy | | Math, Arithmetic Progression |
|C| [Rock Paper Scissors](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e)| [Python](./Round%20C/rock_paper_scissors.py) | _O(N^3)_ | _O(N^3)_ | Medium | | Math, Expected Value, DP, Backtracing |
|D| [Binary Operator](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290)| [Python](./Round%20C/binary_operator.py) [Python](./Round%20C/binary_operator2.py) [Python](./Round%20C/binary_operator3.py) | _O(N * E)_ | _O(N * E)_ | Hard | | Math, Polynomial Calculator, Hash |