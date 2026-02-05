# 2026-02-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.71246  |       1.1131   |   0.098384 |
| solution-1-flask   |     0.468505 |       1.01005  |   0.226531 |
| solution-aron-mark |     0.443098 |       0.163669 |   0.241497 |
| solution-pl        |     0.43547  |       0.163407 |   0.241618 |
| solution-1         |     8.26663  |       1e-06    |   0.62689  |
| solution-2         |     5.06809  |       0.623249 |   0.893658 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.437962 |       0.169308 |   0.36249  |
| solution-pl        |     0.436994 |       0.164621 |   0.362519 |
| solution-flask     |     0.437648 |       1.00908  |   0.384462 |
| solution-1-flask   |     0.442505 |       1.00895  |   0.707507 |
| solution-2         |     0.436085 |       0.498649 |   1.90458  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.440873 |       0.171448 |    1.02954 |
| solution-pl        |     0.439974 |       0.171739 |    1.0348  |
| solution-flask     |     0.436735 |       1.00904  |    1.59372 |
| solution-1-flask   |     0.44753  |       1.00886  |    5.52603 |
| solution-2         |     0.438133 |       0.557169 |   41.0543  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.441875 |       0.199117 |    3.61094 |
| solution-pl        |     0.44014  |       0.199983 |    3.62913 |
| solution-flask     |     0.435945 |       1.00895  |    5.02765 |