import pixray
pixray.reset_settings()
pixray.add_settings(prompts="Rainbow paint brush",
                    drawer="vqgan",
                    aspect="square",
                    outdir="outputs/pyxgen_logo_v2",
                    iterations=200,
                    learning_rate_drops=[20, 70, 95],
                    gamma_lr=0.1,
                    num_cuts=2,
                    batches=5,
                    custom_loss="smoothness:0.5, aesthetic:0.3")
settings = pixray.apply_settings()
pixray.do_init(settings)
pixray.do_run(settings)