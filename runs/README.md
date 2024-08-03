# 2024-08-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19289  |       1.10844  |   0.096716 |
| solution-aron-mark |     0.566673 |       0.103794 |   0.164995 |
| solution-pl        |     1.83199  |       0.10258  |   0.166337 |
| solution-1-flask   |     0.561345 |       1.00918  |   0.258514 |
| solution-1         |     8.19889  |       1e-06    |   0.708493 |
| solution-2         |     4.49642  |       0.632075 |   1.62816  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.543596 |       1.00914  |   0.193238 |
| solution-aron-mark |     0.546155 |       0.101017 |   0.287108 |
| solution-pl        |     0.566765 |       0.105458 |   0.29003  |
| solution-1-flask   |     0.551714 |       1.00863  |   0.765764 |
| solution-2         |     0.549172 |       0.4706   |   4.74003  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550536 |       1.00893  |   0.90218  |
| solution-aron-mark |     0.548048 |       0.112377 |   0.984102 |
| solution-pl        |     0.546425 |       0.111273 |   0.992953 |
| solution-1-flask   |     0.554758 |       1.00939  |   5.47134  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.558847 |       1.00901  |    3.91201 |
| solution-aron-mark |     0.547754 |       0.145836 |    4.01043 |
| solution-pl        |     0.556485 |       0.144825 |    4.02285 |