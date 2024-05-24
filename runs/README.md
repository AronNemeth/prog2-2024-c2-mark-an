# 2024-05-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.40803  |       1.09099  |   0.078764 |
| solution-pl        |     0.695395 |       0.10571  |   0.165703 |
| solution-aron-mark |     6.03695  |       0.104677 |   0.167003 |
| solution-1-flask   |     0.714887 |       1.00912  |   0.270511 |
| solution-1         |     8.28877  |       1e-06    |   0.864395 |
| solution-2         |     0.704964 |       0.464484 |   0.885397 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.699668 |       1.00907  |   0.169249 |
| solution-pl        |     0.698594 |       0.108534 |   0.264444 |
| solution-aron-mark |     0.704787 |       0.107163 |   0.275971 |
| solution-1-flask   |     0.713311 |       1.01011  |   0.804456 |
| solution-2         |     0.702731 |       0.476706 |   4.48309  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.722836 |       1.00948  |   0.7      |
| solution-aron-mark |     0.690992 |       0.115833 |   0.807537 |
| solution-pl        |     0.702427 |       0.116087 |   0.823433 |
| solution-1-flask   |     0.736626 |       1.00915  |   5.79829  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.709931 |       1.00923  |    2.53491 |
| solution-pl        |     0.701164 |       0.15556  |    2.72381 |
| solution-aron-mark |     0.711999 |       0.155472 |    2.77846 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670078 |       1.00913  |    16.0635 |
| solution-aron-mark |     0.672049 |       0.276044 |    21.761  |
| solution-pl        |     0.673655 |       0.278968 |    22.4148 |