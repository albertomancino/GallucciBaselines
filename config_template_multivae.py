TEMPLATE = """experiment:
  dataset: subdatasets_{sub}
  data_config:
    strategy: dataset
    dataset_path: {path}
  splitting:
    test_splitting:
      strategy: random_subsampling
      test_ratio: 0.2
      folds: 1
  top_k: 10
  evaluation:
    cutoffs: [10, 5, 1]
    simple_metrics: [nDCGRendle2020, HR, ItemCoverage, UserCoverage]
    relevance_threshold: 3
  gpu: 0
  models:
    MultiVAE:
      meta:
        save_recs: True
        verbose: True
        hyper_max_evals: 10
        hyper_opt_alg: tpe
        validation_rate: 5
        validation_metric: nDCGRendle2020@10
      lr: [loguniform, -11.5, 0]
      epochs: 100
      batch_size: 512
      intermediate_dim: [300, 400, 500]
      latent_dim: [100, 200, 300]
      dropout_pkeep: [uniform, 0.5, 1]
      reg_lambda: [loguniform, -11.5, 0]
       """
