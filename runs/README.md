# 2025-09-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.476991 |       1.00821  |   0.100718 |
| solution-pl        |     6.10782  |       0.194272 |   0.239652 |
| solution-aron-mark |     0.598055 |       0.153825 |   0.240633 |
| solution-1-flask   |     1.04541  |       1.07289  |   0.266147 |
| solution-2         |     0.484266 |       0.725578 |   0.800223 |
| solution-1         |     7.97661  |       1e-06    |   0.871089 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480764 |       0.153075 |   0.35985  |
| solution-aron-mark |     0.478527 |       0.154325 |   0.366045 |
| solution-flask     |     0.487214 |       1.00831  |   0.378242 |
| solution-1-flask   |     0.487884 |       1.00834  |   0.804817 |
| solution-2         |     0.477719 |       0.498537 |   2.71195  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479932 |       0.161929 |    1.08462 |
| solution-aron-mark |     0.478416 |       0.162992 |    1.1049  |
| solution-flask     |     0.480359 |       1.00835  |    1.58486 |
| solution-1-flask   |     0.484031 |       1.00838  |    5.71058 |
| solution-2         |     0.479234 |       0.557343 |   32.0052  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478541 |       0.19269  |    3.2729  |
| solution-pl        |     0.478191 |       0.196323 |    3.29006 |
| solution-flask     |     0.481313 |       1.00866  |    5.11558 |