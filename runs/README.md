# 2026-06-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1287   |       1.04599  |   0.104382 |
| solution-aron-mark |     0.433668 |       0.151174 |   0.235765 |
| solution-pl        |     5.99173  |       0.176131 |   0.237771 |
| solution-1-flask   |     0.4361   |       1.00836  |   0.268332 |
| solution-1         |     7.49083  |       1e-06    |   0.692447 |
| solution-2         |     0.42635  |       0.727777 |   1.01388  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430856 |       0.150533 |   0.360984 |
| solution-aron-mark |     0.43421  |       0.151813 |   0.361681 |
| solution-flask     |     0.425997 |       1.00829  |   0.392387 |
| solution-1-flask   |     0.438533 |       1.00832  |   0.854577 |
| solution-2         |     0.425205 |       0.513119 |   2.24615  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427361 |       0.155525 |    1.09369 |
| solution-aron-mark |     0.443035 |       0.157933 |    1.09431 |
| solution-flask     |     0.43355  |       1.00835  |    1.63322 |
| solution-1-flask   |     0.436571 |       1.00831  |    5.57116 |
| solution-2         |     0.422966 |       0.562718 |  291.977   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42712  |       0.186149 |    3.88297 |
| solution-aron-mark |     0.429293 |       0.180542 |    3.88506 |
| solution-flask     |     0.429495 |       1.00839  |    5.22849 |