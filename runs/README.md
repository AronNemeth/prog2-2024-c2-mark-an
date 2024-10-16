# 2024-10-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.24741  |       1.10615  |   0.094752 |
| solution-pl        |     6.0277   |       0.103727 |   0.177507 |
| solution-aron-mark |     0.571941 |       0.105501 |   0.184026 |
| solution-1-flask   |     0.561839 |       1.00903  |   0.262623 |
| solution-1         |     7.536    |       1e-06    |   0.587407 |
| solution-2         |     0.574604 |       0.511864 |   1.28446  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.577968 |       1.00911  |   0.195986 |
| solution-pl        |     0.560646 |       0.104719 |   0.293695 |
| solution-aron-mark |     0.582413 |       0.107828 |   0.316362 |
| solution-1-flask   |     0.585998 |       1.00899  |   0.819868 |
| solution-2         |     0.55837  |       0.473783 |   4.2186   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.584244 |       1.00923  |   0.891837 |
| solution-pl        |     0.570127 |       0.113981 |   1.00415  |
| solution-aron-mark |     0.562124 |       0.112472 |   1.05686  |
| solution-1-flask   |     0.565015 |       1.00914  |   5.58928  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.561294 |       0.143713 |    4.24744 |
| solution-aron-mark |     0.585175 |       0.155533 |    4.47116 |
| solution-flask     |     0.557735 |       1.00957  |    4.57977 |