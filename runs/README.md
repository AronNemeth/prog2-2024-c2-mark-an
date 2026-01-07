# 2026-01-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.13686  |       1.04785  |   0.104786 |
| solution-aron-mark |     0.48888  |       0.165336 |   0.253014 |
| solution-pl        |     0.483292 |       0.233457 |   0.255382 |
| solution-1-flask   |     0.489457 |       1.00862  |   0.264405 |
| solution-1         |     9.1783   |       1e-06    |   0.693336 |
| solution-2         |     6.088    |       0.664925 |   1.30073  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.487614 |       1.00873  |   0.376317 |
| solution-aron-mark |     0.481493 |       0.164522 |   0.377678 |
| solution-pl        |     0.485534 |       0.164801 |   0.380477 |
| solution-1-flask   |     0.481669 |       1.00866  |   0.807781 |
| solution-2         |     0.48167  |       0.523349 |   4.38903  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.498549 |       0.169338 |    1.0998  |
| solution-pl        |     0.481211 |       0.175315 |    1.12678 |
| solution-flask     |     0.476733 |       1.00905  |    1.60695 |
| solution-1-flask   |     0.486686 |       1.00876  |    5.61566 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.491402 |       0.192681 |    3.61063 |
| solution-pl        |     0.479494 |       0.193678 |    3.63523 |
| solution-flask     |     0.484342 |       1.00872  |    5.15659 |