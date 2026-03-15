# 2026-03-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.73295  |       1.1594   |   0.097915 |
| solution-pl        |     4.66579  |       0.140838 |   0.218342 |
| solution-aron-mark |     0.452858 |       0.139798 |   0.231705 |
| solution-1-flask   |     0.445601 |       1.00713  |   0.241545 |
| solution-1         |     8.28209  |       1e-06    |   0.566961 |
| solution-2         |     0.421598 |       0.55444  |   1.02395  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429997 |       0.145517 |   0.3332   |
| solution-pl        |     0.426332 |       0.141551 |   0.36146  |
| solution-flask     |     0.420097 |       1.00728  |   0.47342  |
| solution-1-flask   |     0.434046 |       1.00723  |   0.740422 |
| solution-2         |     0.420822 |       0.516657 |   2.57599  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434743 |       0.149737 |    1.02523 |
| solution-aron-mark |     0.426585 |       0.146252 |    1.03695 |
| solution-flask     |     0.440879 |       1.00714  |    1.8723  |
| solution-1-flask   |     0.429111 |       1.00696  |    5.75569 |
| solution-2         |     0.422263 |       0.567842 |   43.3195  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.440985 |       0.179839 |    5.57119 |
| solution-pl        |     0.447425 |       0.184232 |    5.69874 |
| solution-flask     |     0.426535 |       1.00715  |    6.81662 |