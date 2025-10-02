# 2025-10-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.70265  |       1.06498  |   0.102499 |
| solution-pl        |     0.488886 |       0.160425 |   0.246426 |
| solution-aron-mark |     0.501798 |       0.159804 |   0.247159 |
| solution-1-flask   |     0.495281 |       1.00839  |   0.264183 |
| solution-1         |     7.51404  |       1e-06    |   0.742922 |
| solution-2         |     4.44828  |       0.719044 |   0.999012 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.492284 |       0.157698 |   0.370363 |
| solution-pl        |     0.499115 |       0.159569 |   0.372045 |
| solution-flask     |     0.496468 |       1.0086   |   0.381843 |
| solution-1-flask   |     0.503735 |       1.00847  |   0.798955 |
| solution-2         |     0.493832 |       0.525671 |   4.50618  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500693 |       0.16647  |    1.0802  |
| solution-pl        |     0.494658 |       0.167478 |    1.10036 |
| solution-flask     |     0.49255  |       1.00867  |    1.59031 |
| solution-1-flask   |     0.502739 |       1.00886  |    5.62918 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.498581 |       0.200462 |    3.34259 |
| solution-pl        |     0.495754 |       0.202019 |    3.3777  |
| solution-flask     |     0.495695 |       1.00849  |    5.22197 |