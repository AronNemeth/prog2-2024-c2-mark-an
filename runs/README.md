# 2025-11-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.05696  |       1.1981   |   0.102206 |
| solution-pl        |     0.485059 |       0.159902 |   0.244099 |
| solution-aron-mark |     0.478656 |       0.158559 |   0.249256 |
| solution-1-flask   |     0.482219 |       1.00813  |   0.265726 |
| solution-1         |     8.94199  |       1e-06    |   0.688042 |
| solution-2         |     5.92126  |       0.741142 |   1.4004   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479753 |       0.163761 |   0.370266 |
| solution-aron-mark |     0.483    |       0.169209 |   0.373171 |
| solution-flask     |     0.484934 |       1.0087   |   0.375977 |
| solution-1-flask   |     0.483764 |       1.00863  |   0.797464 |
| solution-2         |     0.46983  |       0.525986 |   6.01595  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.488581 |       0.171694 |    1.08886 |
| solution-pl        |     0.482317 |       0.16782  |    1.09715 |
| solution-flask     |     0.471793 |       1.0086   |    1.61784 |
| solution-1-flask   |     0.487659 |       1.00862  |    5.56776 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476189 |       0.195387 |    3.28574 |
| solution-pl        |     0.478205 |       0.197314 |    3.32313 |
| solution-flask     |     0.479652 |       1.00868  |    5.16713 |