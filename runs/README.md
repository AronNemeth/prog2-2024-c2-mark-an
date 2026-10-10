# 2026-10-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.26353  |       1.0513   |   0.102643 |
| solution-aron-mark |     6.13051  |       0.190708 |   0.258115 |
| solution-pl        |     0.441377 |       0.168832 |   0.26549  |
| solution-1-flask   |     0.447372 |       1.00848  |   0.271035 |
| solution-1         |     8.06103  |       1e-06    |   0.685682 |
| solution-2         |     0.438712 |       0.718227 |   0.784954 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.440152 |       1.00865  |   0.243484 |
| solution-pl        |     0.43351  |       0.171069 |   0.395379 |
| solution-aron-mark |     0.442462 |       0.172912 |   0.40203  |
| solution-1-flask   |     0.447986 |       1.00862  |   0.797236 |
| solution-2         |     0.445858 |       0.530217 |   4.73693  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.435273 |       1.00872  |    1.04621 |
| solution-pl        |     0.438427 |       0.198689 |    1.18302 |
| solution-aron-mark |     0.446531 |       0.175916 |    1.18661 |
| solution-1-flask   |     0.442685 |       1.00895  |    5.57769 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438292 |       0.20374  |    3.69216 |
| solution-pl        |     0.438167 |       0.203438 |    3.69832 |
| solution-flask     |     0.436604 |       1.00873  |    4.3837  |