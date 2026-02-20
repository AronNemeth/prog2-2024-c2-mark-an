# 2026-02-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.50489  |       1.04979  |   0.103943 |
| solution-aron-mark |     0.440846 |       0.147809 |   0.228347 |
| solution-pl        |     0.440978 |       0.145853 |   0.229254 |
| solution-1-flask   |     0.460934 |       1.00848  |   0.269959 |
| solution-1         |     7.34917  |       1e-06    |   0.687373 |
| solution-2         |     4.30563  |       0.677595 |   0.902275 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444314 |       0.147219 |   0.351966 |
| solution-aron-mark |     0.443681 |       0.145956 |   0.35642  |
| solution-flask     |     0.441459 |       1.00852  |   0.369944 |
| solution-1-flask   |     0.445073 |       1.00829  |   0.801748 |
| solution-2         |     0.437822 |       0.508178 |  13.635    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.456784 |       0.153313 |    1.0709  |
| solution-aron-mark |     0.447213 |       0.154542 |    1.09084 |
| solution-flask     |     0.440266 |       1.00857  |    1.56763 |
| solution-1-flask   |     0.447871 |       1.0087   |    5.6041  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.441152 |       0.180767 |    3.72359 |
| solution-pl        |     0.439765 |       0.179742 |    3.72378 |
| solution-flask     |     0.440137 |       1.00866  |    5.07663 |