# 2026-11-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.438926 |       1.00859  |   0.103739 |
| solution-aron-mark |     3.28716  |       0.168804 |   0.253771 |
| solution-pl        |     0.432371 |       0.169875 |   0.257586 |
| solution-1-flask   |     2.79501  |       1.15218  |   0.271615 |
| solution-1         |    10.0272   |       1e-06    |   0.604711 |
| solution-2         |     5.48379  |       0.564716 |   1.47392  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.473349 |       1.00891  |   0.236567 |
| solution-aron-mark |     0.444314 |       0.170912 |   0.394959 |
| solution-pl        |     0.462303 |       0.183822 |   0.40322  |
| solution-1-flask   |     0.484202 |       1.00886  |   0.823087 |
| solution-2         |     0.43749  |       0.552857 |   2.52787  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.438544 |       1.00894  |    1.02852 |
| solution-pl        |     0.449677 |       0.183494 |    1.15308 |
| solution-aron-mark |     0.438344 |       0.182    |    1.17004 |
| solution-1-flask   |     0.44131  |       1.00866  |    5.73422 |
| solution-2         |     0.450921 |       0.595495 |   27.1975  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433528 |       0.214259 |    3.67305 |
| solution-pl        |     0.437291 |       0.217118 |    3.73553 |
| solution-flask     |     0.432717 |       1.00898  |    4.40716 |