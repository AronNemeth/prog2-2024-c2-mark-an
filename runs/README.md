# 2026-03-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.7809   |       1.0455   |   0.107784 |
| solution-pl        |     4.91992  |       0.14714  |   0.234187 |
| solution-aron-mark |     0.441965 |       0.14646  |   0.23676  |
| solution-1-flask   |     0.447184 |       1.0085   |   0.270333 |
| solution-1         |     8.14801  |       1e-06    |   0.698592 |
| solution-2         |     0.443028 |       0.626746 |   0.844591 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.44393  |       0.150365 |   0.364997 |
| solution-aron-mark |     0.444156 |       0.150303 |   0.368823 |
| solution-flask     |     0.444949 |       1.00869  |   0.387098 |
| solution-1-flask   |     0.450721 |       1.0088   |   0.789716 |
| solution-2         |     0.440482 |       0.507772 |   3.41493  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461316 |       0.156056 |    1.10826 |
| solution-aron-mark |     0.445727 |       0.157102 |    1.13103 |
| solution-flask     |     0.441655 |       1.00888  |    1.61163 |
| solution-1-flask   |     0.448357 |       1.0088   |    5.64025 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445764 |       0.183578 |    3.99985 |
| solution-pl        |     0.446045 |       0.181481 |    4.02291 |
| solution-flask     |     0.444301 |       1.00866  |    5.19498 |