# 2026-02-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.53385  |       1.06096  |   0.101512 |
| solution-aron-mark |     0.454953 |       0.146155 |   0.231183 |
| solution-pl        |     0.451815 |       0.14732  |   0.233529 |
| solution-1-flask   |     0.453775 |       1.00836  |   0.260487 |
| solution-1         |     7.3744   |       1e-06    |   0.871716 |
| solution-2         |     4.47442  |       0.785131 |   1.16418  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464975 |       0.147641 |   0.357436 |
| solution-aron-mark |     0.446431 |       0.148227 |   0.361313 |
| solution-flask     |     0.454812 |       1.00852  |   0.373164 |
| solution-1-flask   |     0.45429  |       1.00858  |   0.794797 |
| solution-2         |     0.444856 |       0.514582 |  14.3987   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.441641 |       0.154943 |    1.08465 |
| solution-aron-mark |     0.449883 |       0.1535   |    1.09615 |
| solution-flask     |     0.446169 |       1.00862  |    1.58122 |
| solution-1-flask   |     0.445199 |       1.00857  |    5.61164 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447874 |       0.178655 |    3.77071 |
| solution-aron-mark |     0.442236 |       0.179601 |    3.78547 |
| solution-flask     |     0.446723 |       1.00867  |    5.12676 |