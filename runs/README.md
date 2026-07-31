# 2026-07-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.48212  |       1.0092   |   0.101226 |
| solution-1-flask   |     1.28878  |       1.04863  |   0.230426 |
| solution-aron-mark |     0.463624 |       0.159638 |   0.241161 |
| solution-pl        |     0.449907 |       0.157442 |   0.248761 |
| solution-1         |     8.18701  |       1e-06    |   0.659785 |
| solution-2         |     4.93317  |       1.21287  |   0.848363 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.451242 |       0.159307 |   0.362317 |
| solution-pl        |     0.452844 |       0.161716 |   0.36676  |
| solution-flask     |     0.457188 |       1.00928  |   0.395137 |
| solution-1-flask   |     0.462845 |       1.00936  |   0.728611 |
| solution-2         |     0.448189 |       0.533597 |  11.52     |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465872 |       0.167372 |    1.05462 |
| solution-pl        |     0.45403  |       0.165956 |    1.06933 |
| solution-flask     |     0.451309 |       1.00953  |    1.70334 |
| solution-1-flask   |     0.502521 |       1.0093   |    5.7516  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.445726 |       0.188069 |    3.70472 |
| solution-aron-mark |     0.452204 |       0.189378 |    3.81219 |
| solution-flask     |     0.459154 |       1.00936  |    5.54697 |