# 2025-04-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06763  |       1.12899  |   0.084068 |
| solution-aron-mark |     0.506242 |       0.122941 |   0.194709 |
| solution-pl        |     6.97366  |       0.121559 |   0.196046 |
| solution-1-flask   |     0.511698 |       1.00862  |   0.266227 |
| solution-1         |     7.28946  |       1e-06    |   0.654586 |
| solution-2         |     0.507472 |       0.58496  |   0.722401 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.507097 |       0.123429 |   0.29509  |
| solution-aron-mark |     0.508334 |       0.121716 |   0.295469 |
| solution-flask     |     0.506976 |       1.00925  |   0.298359 |
| solution-1-flask   |     0.513097 |       1.00896  |   0.783549 |
| solution-2         |     0.50895  |       0.50335  |   3.83205  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.505507 |       0.128605 |   0.903495 |
| solution-aron-mark |     0.50829  |       0.127923 |   0.909331 |
| solution-flask     |     0.508765 |       1.00876  |   1.29651  |
| solution-1-flask   |     0.51165  |       1.00857  |   5.37898  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.501868 |       0.159745 |    2.81163 |
| solution-pl        |     0.501525 |       0.161432 |    2.82169 |
| solution-flask     |     0.505614 |       1.00847  |    4.23977 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50446  |       0.276275 |    15.9212 |
| solution-aron-mark |     0.509521 |       0.268844 |    16.0052 |