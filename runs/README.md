# 2025-03-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.572284 |       1.0094   |   0.08514  |
| solution-aron-mark |     1.85694  |       0.128788 |   0.193816 |
| solution-pl        |     0.532521 |       0.132996 |   0.198292 |
| solution-1-flask   |     5.20402  |       1.05506  |   0.269744 |
| solution-1         |     7.7237   |       1e-06    |   0.688354 |
| solution-2         |     0.524872 |       0.597141 |   1.47817  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550388 |       0.127564 |   0.29851  |
| solution-aron-mark |     0.562534 |       0.129653 |   0.304629 |
| solution-flask     |     0.544481 |       1.00955  |   0.339265 |
| solution-1-flask   |     0.56465  |       1.00964  |   0.814178 |
| solution-2         |     0.561971 |       0.543266 |   2.49397  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.523526 |       0.129687 |   0.900169 |
| solution-aron-mark |     0.527411 |       0.134943 |   0.902483 |
| solution-flask     |     0.537832 |       1.0092   |   1.26735  |
| solution-1-flask   |     0.557014 |       1.00947  |   5.93641  |
| solution-2         |     0.561735 |       0.602733 | 180.226    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529068 |       0.158435 |    2.88282 |
| solution-pl        |     0.527639 |       0.161062 |    2.93323 |
| solution-flask     |     0.514608 |       1.00915  |    4.29709 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529454 |       0.265281 |    18.4525 |
| solution-pl        |     0.540421 |       0.264711 |    19.0142 |