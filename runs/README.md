# 2024-08-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554099 |       1.00907  |   0.089912 |
| solution-aron-mark |     1.85885  |       0.104176 |   0.169372 |
| solution-pl        |     0.557822 |       0.103006 |   0.172876 |
| solution-1-flask   |     1.22432  |       1.09698  |   0.258986 |
| solution-1         |     7.63394  |       1e-06    |   0.575657 |
| solution-2         |     4.50749  |       0.558539 |   1.1913   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.557323 |       1.00944  |   0.230494 |
| solution-aron-mark |     0.551946 |       0.10654  |   0.297632 |
| solution-pl        |     0.55871  |       0.104443 |   0.300892 |
| solution-1-flask   |     0.559614 |       1.00889  |   0.779485 |
| solution-2         |     0.554241 |       0.473163 |   2.88106  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.556262 |       1.00928  |   0.908146 |
| solution-pl        |     0.554383 |       0.112758 |   1.01714  |
| solution-aron-mark |     0.554113 |       0.113554 |   1.01805  |
| solution-1-flask   |     0.556814 |       1.00924  |   5.54092  |
| solution-2         |     0.558736 |       0.524182 | 295.728    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55256  |       1.00996  |    4.2278  |
| solution-pl        |     0.553256 |       0.145372 |    4.34501 |
| solution-aron-mark |     0.555264 |       0.149663 |    4.44467 |